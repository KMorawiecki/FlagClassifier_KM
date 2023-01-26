from DatasetAugmentation import ImageAugmentator, LabelSorter


FLAG_WIDTH = 120
FLAG_HEIGHT = 80
FLAG_DIR = 'flags'

ls = LabelSorter.LabelSorter()
ls.sort_labels_in_dir(FLAG_DIR)

ia = ImageAugmentator.ImageAugemtator(FLAG_DIR, FLAG_WIDTH, FLAG_HEIGHT)
ia.create_image_variations()
