# Preparing the environment:

1. Create a new virtualenv with Python 3.8
2. Install packages with `pip install -r requirements.txt`

# Preparing the model
For preparing the flag dataset firstly use command `scrapy crawl flags`.
Then run `python augment_dataset.py`

The pretrained model already exists in the "mlp" folder. 
If you wish to redo all the steps, use `python train.py` command.
This will prepare a new model in the "mlp_new" folder. 
The model is fairly simple with only 6 epochs of training, so it should be quick.

# Using the inference path

Copy the test flags into the "TestFlags" folder. Make sure they have .jpg extension.
Run the inference path with `python inference_path mlp` or `python inference_path mlp_new`, 
depending on if you want to run the pretrained model or newly trained one.