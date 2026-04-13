import requests as req

info = "easy-get - программа для минимального взаимодействия с интернетом\n easy-get post/get (url)\n"

def start_module(args):
	if len(args) < 1 or not args[1]:
		print("введите корректные аргументы")
		return
	if args[0] == "get":
		get = req.get(args[1])
		print(get.text)
	if args[0] == "post":
		get = req.post(args[1])
