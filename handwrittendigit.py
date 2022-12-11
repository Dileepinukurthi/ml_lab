import numpy as np
import cv2
import onnxruntime
model = "mnist-12.onnx" # will be provided
image = cv2.imread('dig3.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray,(28,28)).astype(np.float32)/255
inputImg = np.reshape(gray,(1,1,28,28))
session = onnxruntime.InferenceSession(model,None)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
result = session.run([output_name],{input_name:inputImg})
print(result)
prediction = int(np.argmax(result[0].squeeze()))
print(prediction)
