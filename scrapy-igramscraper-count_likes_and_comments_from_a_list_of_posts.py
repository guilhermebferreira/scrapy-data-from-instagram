from igramscraper.instagram import Instagram
import csv



username = input("Digite o seu usuário do Instagram, sem a arroba, e aperte < ENTER >.\n")
password = input("Digite a senha do Instagram, e aperte < ENTER >.\n")

instagram = Instagram()
instagram.with_credentials(username, password)
instagram.login()

#codigos das postagens que deseja inspecionar
posts_total = ['B7JZIK2AWg4', 'B7G2ECqAZ1N' ]
#caso já tenha executados uma inspeção parcial anteriormente, você pode colocar abaixo os códigos das postagens que deverão ser ignoradas
posts_importados = []
posts= list(set(posts_total) - set(posts_importados))

with open('insta_output.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	count = 0
	for post in posts:
		# print('#', count, ' code:', post)
		comments = instagram.get_media_comments_by_code(post, 10000)
			
		c = len(comments['comments'])
		likes = instagram.get_media_likes_by_code(post, 1000)
		l = len(likes['accounts'])
		print(post, ',', "https://www.instagram.com/p/"+post,',', c, ',',l)
		# try:
			
		# 	# media = instagram.get_media_by_url("https://www.instagram.com/"+post)

		# 	comments = instagram.get_media_comments_by_code(post, 10000)
			
		# 	c = len(comments['comments'])
		# 	# print(c)
		# 	likes = instagram.get_media_likes_by_code(post, 1000)
		# 	l = len(likes['accounts'])
		# 	# print(likes)
		# 	# print(l)
		# 	print(post, ',', "https://www.instagram.com/p/"+post,',', c, ',',l)
		# 	writer.writerow(post, c, l)
		# except Exception as e:
		# 	pass
		count += 1
