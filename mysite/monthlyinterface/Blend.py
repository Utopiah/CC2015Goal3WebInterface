# coding: utf-8

# # Integrate the result back in Django
# 
# ## Minimum
# 1. load only the required functions
# 1. modify them to save to database
# 1. provide the result to be able to iterate on generation TODO
# 
# ## Optional
# 1. use generators TODO

#imports are done inside functions in order to distinguish domain specific functions from the rest
def pathInit():
    import os
    for directory in ['creations','materials']:
        if not os.path.exists(directory):
            os.makedirs(directory)

def blendNewImagesFromThemes(Themes, imageSize=50, opacity=0.7):
    pathInit()
    creationsPath = 'creations/'
    loadedImages = []
    loadedURLs = []
    images = []
    urls = []
    for Theme in Themes:
        #for the moment assuming 2 themes or less
        images = addImageToLibrary(Theme, 10)
        if len(Themes) == 1:
            [images, urls] = loadingImages(images, 1)
        else:
            [images, urls] = loadingImages(images, 2)
        loadedImages.extend(images)
        loadedURLs.extend(urls) 
    blendedImage = imagesBlend(loadedImages, imageSize, opacity)
    result = dict(image=blendedImage,
                  theme=Themes, 
                  imageSize=imageSize, 
                  opacity=opacity,
                  filePath='',
                  usedURLs=loadedURLs[:2])
    
    import hashlib
    from PIL import Image
    usedConfiguration = '_'.join(result['usedURLs'])+'_'.join(Theme)+str(imageSize)+str(opacity)
    image_path = creationsPath+hashlib.md5(usedConfiguration.encode('utf-8')).hexdigest()
    image_path += ".jpg"
    creation = Creation(file_path=image_path, opacity=opacity, image_size=imageSize,
                        pub_date=timezone.now(),
                        desired_format=Desired_Format.objects.get(id=1),
                        desired_theme=','.join(Themes),
                        user_id=1)
    creation.save()
    m0 = Material.objects.filter(source_url=loadedURLs[0])
    m1 = Material.objects.filter(source_url=loadedURLs[1])
    creation.materials.add(*m0, *m1)
    saveGeneratedImageToLibrary(image_path,result['image'])
    return result

def isMaterialPresent(materialURL):
    matches = Material.objects.filter(source_url=materialURL).count()
    #might use a hash instead, could also be moved directly to the models
    if (matches>0):
        return True
    else :
        return False
    
def imagesBlend(loadedImages, imageSize, opacity):
    #rint(imageSize, type(imageSize))
    from PIL import Image
    # limited to 2 images only
    cleanDB = []
    for image in loadedImages:
        resizedImage = image.resize((imageSize, imageSize))
        coherentImage = resizedImage.convert('RGBA')
        cleanDB.append(coherentImage)
    return Image.blend(cleanDB[0], cleanDB[1], opacity)

def loadingImages(images, limit):
    from PIL import Image
    db = images["images"]
    loadedImages = []
    loadedURLs = []
    materialsUsed = 0
    for imageIndex in range(0, limit):
        if isMaterialPresent(db[imageIndex]["imageurl"]):
            materialsUsed+=1
            matches = Material.objects.filter(source_url=db[imageIndex]["imageurl"])

            #print(matches, matches[0], matches[0].file_path)
            image = Image.open(matches[0].file_path)
        else:
            image = getImageFromUrl(db[imageIndex]["imageurl"])
        loadedImages.append(image)
        # should check first if image already present
        loadedURLs.append(db[imageIndex]["imageurl"])
    if materialsUsed > 1:
        print('Warning: probably dupe.')
    return [loadedImages, loadedURLs]

def getImageFromUrl(imageurl):
    materialsPath = 'materials/'
    import hashlib
    import urllib.request
    from PIL import Image
    import io
    fd = urllib.request.urlopen(imageurl)
    image_file = io.BytesIO(fd.read())
    
    image_path = materialsPath+hashlib.md5(imageurl.encode('utf-8')).hexdigest()
    image_path += ".jpg"
    material = Material(file_path=image_path, source_url=imageurl, desired_format=Desired_Format.objects.get(id=1))
    material.save()
    loadedImage = Image.open(image_file)
    # convert required http://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
    loadedImage.convert('RGB').save(image_path)
    return loadedImage
    # might be costly, when and how can it be closed later on?
    
def addImageToLibrary(keyword, amount):
    import urllib.request
    import json
    searchUrl = "http://api.pixplorer.co.uk/image?word=" + keyword + "&size=tb&amount=" + str(amount)
    with urllib.request.urlopen(searchUrl) as response:
        myJson = response.read().decode('utf-8')
        deserialized_output = json.loads(str(myJson))
    return deserialized_output

def saveGeneratedImageToLibrary(file_path, image):
    # e.g. saveGeneratedImageToLibrary('test.bmp', result['image'])
    from PIL import Image
    # convert required http://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
    image.convert('RGB').save(file_path)
    # improper, see name hashing done before, replicate while taking into account blending parameters
    img = Image.open(file_path)
    # should also update the database accordingly to
        # serve the result back to the user
        # prevent the result from being generated again
        # allow forks
    return img


# ### To faciliate database testing
# * http://eli.thegreenplace.net/2014/02/20/clearing-the-database-with-django-commands

# usage examples
	# blendNewImagesFromThemes(['Maldives','Diving'])

def BlendMe(arguments)
	result = blendNewImagesFromThemes(['Maldives','Diving'])
    return result.filePath
    # should return instead the ID then redirect there
