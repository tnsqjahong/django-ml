import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image


class SDImageCreator:
    api_key = "b4e4ec34-b0e3-4749-94dd-1dce35394c5f"
    model_key = "df97c5a2-ccd1-4a38-b345-d3a9fd8ead97" # "YOUR_MODEL_KEY"
    # model_inputs = {
    #     # a json specific to your model. For example:
    #     "imageURL":  "https://demo-images-banana.s3.us-west-1.amazonaws.com/image2.jpg"
    # }
    def create_image(self, input_data):
        model_inputs = {
            "prompt": input_data["data"],
            "num_inference_steps":50,
            "guidance_scale":9,
            "height":512,
            "width":512,
            "seed":3242
        }

        # Run the model
        out = banana.run(self.api_key, self.model_key, model_inputs)

        # Extract the image and save to output.jpg
        image_byte_string = out["modelOutputs"][0]["image_base64"]
        image_encoded = image_byte_string.encode('utf-8')
        image_bytes = BytesIO(base64.b64decode(image_encoded))
        image = Image.open(image_bytes)


        return image

if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    alg = SDImageCreator()
    data = {
        "data": "muffin"
    }
    response = alg.create_image(data)
    print(response)