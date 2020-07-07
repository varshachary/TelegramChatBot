import telepot
#Basic commands to experiment the API
bot =telepot.Bot('1274886478:AAEnBI3cv-tFGdD3hMeGNXzb8nLfm222wQA')
print(bot.getMe())
#prints id,firstname,llastname,typ,date ad text received
print(bot.getUpdates())
