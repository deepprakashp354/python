class Dataset(object):
	def __init__(self,data=None):
		self.data=data

class MRIDataset(Dataset): #inheriting the class Dataset
	def __init__(self, data=None, parameters=None):
		#here has the same effect as calling
		#Dataset.__init__(self)
		super(MRIDataset, self).__init(data)
		self.parameters=parameters
		print(self.parameters)

mri=MRIDataset(data=[1,2,3])