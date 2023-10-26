import matplotlib.pyplot as plt
import io

class Loading_Data:

    # Function to load image and mask data from an S3 bucket
    def loading_data(self, s3, default_location):
        img_data_array = []  # List to store image data
        mask_data_stack = []  # List to store mask data

        print("Reading the images")
        s3_bucket = "appledatabucket"  # Specify the S3 bucket name
        keys = []  # List to store object keys in the S3 bucket

        # Collect object keys from the S3 bucket
        for obj in s3.Bucket(s3_bucket).objects.all():
            keys.append(obj.key)

        # Iterate through the object keys
        for key in keys:
            file_stream = io.BytesIO()
            s3.Bucket(s3_bucket).Object(key).download_fileobj(file_stream)

            if ".jpg" in key and "Apple" in key:
                # Load and store image data
                print(key)
                img = plt.imread(file_stream, format='jpg')
                print(img.shape)
                img_data_array.append(img)

            elif ".tiff" in key and "Apple" in key:
                # Load and store mask data
                mask = plt.imread(file_stream, format='tiff')
                print(mask.shape)
                mask_data_stack.append(mask)

        return img_data_array, mask_data_stack
