def GetPredection(model, inputs: list):
  result = {
                0: "Iris-setosa",
                1: "Iris-versicolor",
                2: "Iris-virginica"}
  
  predections = model.predict([inputs])[0]
  
  return result[predections]
