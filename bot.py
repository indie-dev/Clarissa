import os
import sys as sys


os.system("python bot/bot.py engage")
import bot_response as bot
import bot_learn as learner

def hasUserSwore(message):
        if "fuck" in message:
                return True
        elif "bitch" in message:
                return True
        elif "Fuck" in message:
                return True
        elif "Bitch" in message:
                return True
        else:
                return False

#Allow the user to communicate with the bot
#Also allow the bot to learn about the person

def toBot():
        if(os.path.isfile(".bot_engage")):
                print "You can only run one instance of Clarissa."
        else:
                swearNum = 1
                messageToBot = raw_input("Message: ")
                if(messageToBot == "--add-command"):
                        writeCommand(command=raw_input("Command: "), response=raw_input("Responses: "))
                        reload(bot)
                elif(messageToBot == "kill-bot"):
                        exit()
        	elif(messageToBot == "--clear-commands"):
                	#os.remove("commands.bot")
                	#os.remove("responses.bot")
                        os.remove("bot_response.py")
                        writeCommand("Hello", "Hi")
                        print "Cleared commands"
                elif(messageToBot == "learn"):
                        learner.learn(db_support=False)
                elif(messageToBot == "--get-commands"):
                        commandsList = open("commands.list","r")
                        print commandsList.read()
                bot.getResponse(messageToBot)
                toBot()



def writeCommand(command, response):
	file = open("bot_response.py", "a")
	file.write("\n\telif(messageToBot == \""+command+"\"):")
	file.write("\n\t\tprint \"Clarissa: "+response+"\"")
	file.flush()
	file.close()

	commandList = open("commands.list", "w")
	commandList.write(command)
	commandList.flush()
	commandList.close()

def getIf(message, command, response):
	if(message == command):
		print "Clarissa: "+response
	else:
		print "I do not understand "+message

def getCommands():
	return open("commands.bot", "r").read()

def getResponses():
	return open("responses.bot", "r").read()


swearNum = 0

try:
        if(sys.argv[1] == "--add-command"):
                writeCommand(command=sys.argv[2], response=sys.argv[3])
        	reload(bot)
        elif (sys.argv[1] == "--clear-commands"):
                #os.remove("commands.bot")
                #os.remove("responses.bot")
                os.remove("bot_response.py")
                writeCommand("Hello", "Hi")
                print "Cleared commands"
        elif (sys.argv[1] == "learn"):
                learner.learn(db_support=False)
        elif (sys.argv[1] == "--get-commands"):
                commandsList = open("commands.list","r")
                print commandsList.read()
        else:
                toBot()
except IndexError:
        toBot()
