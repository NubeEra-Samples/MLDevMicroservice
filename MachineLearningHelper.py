class MLHelper:
    def __init__(self) -> None:
        self.defaultMessage="Welcome to ML/AI Project <br /><a href='./loadds'>01.Load DataSet</a>"
        print("Class Loaded...")
    def loadDataSet(self,strDataSetName) -> str:
        self.dataset=None
        if strDataSetName=="iris":
            from sklearn.datasets import load_iris
            self.dataset=load_iris()
        strResult="""
        Data Set Loaded Successfully...<br />
        Click <a href='./trainsplit'>Here</a> to 02.Train & Split DataSet<br />
        """
        return strResult
    def trainNTestSplitDS(self) -> str:        
        X=self.dataset.data #Questions/Properties
        Y=self.dataset.target #Answers/Result/Label

        from sklearn.model_selection import train_test_split
        self.X_train,self.X_test,self.Y_train,self.Y_test=train_test_split(X,Y,random_state=50,test_size=0.25)
        strResult="""
        Train,Test and Split done Successfully...<br />
        Click <a href='./startMLLearning'>Start Learning</a><br />
        """
        return strResult
    def startMLLearning(self) -> bool:
        from sklearn.tree import DecisionTreeClassifier
        clf=DecisionTreeClassifier()
        clf.fit(self.X_train,self.Y_train)
        return True