class MpTopo:
	mininetBuilder = "mininet"
	multiIfTopo = "MultiIf"
	ECMPLikeTopo = "ECMPLike"
	topoAttr    = "topoType"
	switchNamePrefix = "s"
	routerNamePrefix = "r"
	clientName = "Client"
	serverName = "Server"
	routerName = "Router"
	cmdLog = "command.log"

	"""Simple MpTopo"""
	def __init__(self, topoBuilder, topoParam):
		self.topoBuilder = topoBuilder
		self.topoParam = topoParam
		self.logFile = open(MpTopo.cmdLog, 'w')
	
	def commandTo(self, who, cmd):
		self.logFile.write(who.__str__() + " : " + cmd + "\n")
		self.topoBuilder.commandTo(who, cmd)

	def getHost(self, who):
		return self.topoBuilder.getHost(who)

	def addHost(self, host):
		return self.topoBuilder.addHost(host)

	def addSwitch(self, switch):
		return self.topoBuilder.addSwitch(switch)

	def addLink(self, fromA, toB, **kwargs):
		self.topoBuilder.addLink(fromA,toB,**kwargs)

	def getCLI(self):
		self.topoBuilder.getCLI()

	def startNetwork(self):
		self.topoBuilder.startNetwork()
	
	def closeLogFile(self):
		self.logFile.close()

	def stopNetwork(self):
		self.topoBuilder.stopNetwork()
