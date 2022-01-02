#1. Include Packages
import flask
import MachineLearningHelper

#2. Create an object
objFlask=flask.Flask(__name__)
mlh=MachineLearningHelper.MLHelper()

#3. Address Bind with Declare Function
@objFlask.route("/startMLLearning",methods=["GET"])
def startMLLearning():
	result=mlh.startMLLearning()
	return result

@objFlask.route("/trainsplit",methods=['GET'])
def trainnsplitds():
	strResult=mlh.trainNTestSplitDS()
	return strResult

@objFlask.route("/loadds",methods=['GET'])
def loadds():
	strResult=mlh.loadDataSet("iris")
	return strResult

@objFlask.route("/",methods=['GET'])
def default():
	return mlh.defaultMessage

#4. Run Application
objFlask.run(host="0.0.0.0",port=80)
