#!/usr/bin/env python3

import argparse
import sys, os
import platform
import requests
import subprocess
import webbrowser

# Clean the screen of the terminal 
def cleanScreen():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux" or "Darwin":
		subprocess.call(["clear"])
cleanScreen()

# set a list of defined arguments that can be used for 
# seperate options
def arguments():
	parser = argparse.ArgumentParser()

	# used to specify user
	parser.add_argument(
		"-u", "--user", 
		help="Define username to search for.", 
		action="store")
	# set timeout for webpage request, may delete
	parser.add_argument("-t", "--timeout", 
		help="Set request timeout.", 
		action="store")
	# allows requests module to check redirected webpages
	parser.add_argument("-r", "--allow-redirects", 
		help="Set redirections for websites. May show false positives.", 
		action="store_true")
	# will open pages automatically so user does not have to
	parser.add_argument("-o", "--open-pages", 
		help="Prompts webbrowser to open found URL's.", 
		action="store_true")
	# change user agent
	parser.add_argument("-a", "--user-agent", 
		help="Change user agent.", 
		action="store")
	parser.add_argument("-l", "--list-agents",
		help="List available user agents.",
		action="store_true")
	parser.add_argument("-w", "--write",
		help="Write findings to file.",
		action="store_true")
	parser.add_argument("-v", "--version",
		help="Version information.",
		action="store_true")
	
	args = parser.parse_args()

	return args

# all sites checked in profiler
def manageSites():
	sites = [
		f"https://www.instagram.com/{arguments().user}/", # Instagram
		f"https://www.facebook.com/{arguments().user}", #Facebook
		f"https://twitter.com/{arguments().user}/", # Twitter
		f"https://www.pinterest.com/{arguments().user}/", # Pinterest
		#f"https://myspace.com/{arguments().user}", # Myspace # verify=False to pass SSL certificate
		f"https://www.pornhub.com/users/{arguments().user}", # Pornhub
		f"https://www.xvideos.com/profiles/{arguments().user}/", # Xvideos
		#f"https://www.meetme.com/{user}/", # Meetme
		f"https://badoo.com/profile/{arguments().user}/", # Badoo
		#f"http://www.blackplanet.com/{user}", # Blackplanet
		f"https://www.reddit.com/user/{arguments().user}/", # Reddit
		f"https://www.youtube.com/user/{arguments().user}", # Youtube
		f"https://ask.fm/{arguments().user}", # askfm
		f"https://open.spotify.com/user/{arguments().user}", # spotify
		f"https://soundcloud.com/{arguments().user}", # Soundcloud
		f"https://www.xboxgamertag.com/search/{arguments().user}/", # XBOX
		f"https://psnprofiles.com/{arguments().user}", # Playstation
		#f"https://piknu.com/u/{arguments().user}", # Piknu
		f"https://profiles.wordpress.org/{arguments().user}", # Wordpress
		f"http://user.dtcc.edu/~{arguments().user}/", # DTCC users
		#f"https://www.free-datehookup.com/{arguments().user}", # Date Hookup
		f"https://profiles.wordpress.org/{arguments().user}", # Wordpress
		#f"https://bitbucket.org/{arguments().user.upper()}/", # Bitbucket
		f"https://bitbucket.org/{arguments().user}/", # Bitbucket
		f"https://github.com/{arguments().user}", # Github
		f"https://{arguments().user}.blogspot.com/", # Blogspot
		f"https://www.etsy.com/people/{arguments().user}", # Etsy
		f"https://about.me/{arguments().user}", # About me
		f"https://imgur.com/user/{arguments().user}", # imgur
		f"http://{arguments().user}.tumblr.com", # tumblr
		f"https://foursquare.com/{arguments().user}", # foursquare
		f"https://mix.com/{arguments().user}", # Mix / StumbleUpon
		f"https://www.kiwibox.com/{arguments().user}", # kiwibox
		f"https://www.reverbnation.com/{arguments().user}", # Reverb Nation
		f"http://us.viadeo.com/en/profile/{arguments().user}", # Viadeo
		f"https://www.gaia.com/person/{arguments().user}", # gaia
f"https://weheartit.com/{arguments().user}", # We Heart it
		f"https://www.deviantart.com/{arguments().user}", # Deviant art
		f"https://www.flickr.com/photos/{arguments().user}", # Flickr
		f"https://www.quora.com/profile/{arguments().user}", # Quora
		#f"https://instadp.site/{arguments().user}", # instaDP
		#f"https://steamcommunity.com/id/{arguments().user}", # steam
		#f"https://steamidfinder.com/lookup/{arguments().user}", # Alternative to steam
		f"https://www.reverbnation.com/{arguments().user}/", # Reverb nation
		f"https://imageshack.us/user/{arguments().user}", # Imageshack
f"https://{arguments().user}.livejournal.com", # Live journal
			f"https://www.zillow.com/profile/{arguments().user}/", # Zillow
				f"http://photobucket.com/user/{arguments().user}/library/", # Photobucket, needs redirect on
f"https://www.tripadvisor.com/Profile/{arguments().user}", #Trip Advisor
f"https://www.linkedin.com/in/{arguments().user}/", #LinkedIn
f"https://plus.google.com/+{arguments().user}", #Google Plus
f"https://venmo.com/{arguments().user}", #Venmo
f"https://poshmark.com/closet/{arguments().user}", #Poshmark
f"https://ello.co/{arguments().user}", #Ello
f"https://www.quora.com/profile/{arguments().user}",#Quora
f"https://www.periscope.tv/{arguments().user}/", #Periscope
f"https://medium.com/{arguments().user}", #Medium
#f"https://lipsiapp.com/{arguments().user}", #lipsiapp
f"https://www.viewbug.com/member/{arguments().user}", # Viewbug
#f"https://www.twitch.tv/{arguments().user}", # Twitch
#f"https://www.modelmayhem.com/{arguments().user}", # Model Mayhem
#f"https://itsmyurls.com/{arguments().user}", # My Urls
f"https://vsco.co/{arguments().user}/images/1", # Vsco
f"https://www.girlsaskguys.com/user/{arguments().user}", # Girls ask Guys
f"https://cash.me/{arguments().user}", #cash me page
f"https://about.me/{arguments().user}", # about me 
f"https://www.paypal.me/{arguments().user}", # paypal
f"https://quizlet.com/{arguments().user}", # quizlet 
f"https://www.myfitnesspal.com/{arguments().user}", # myfitnesspal


	]

	return sites

def version():
	print("""
		\t    |P|R|O|F|I|L|E|R|
		       ---------------------------
		
		\tWritten by: Matthew Greer
		\tVersion: 2.0


			,
		            ((_,-.
		             '-.\\_)'-,
		                 )  _ )'-   
		       ,.;.,;,,(/(/ \\));,;.,.,

		""")

def agents():
	if arguments().user_agent.lower() == 'chrome':
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
		}
	elif arguments().user_agent.lower() == 'firefox':
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
		}
	elif arguments().user_agent.lower() == 'safari':
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Mwendo/1.1.5 Safari/537.21"
		}

		return headers

def listAgents():
	print("""
		\tUser-Agents
		       -------------
		\t1)	Chrome
		\t2)	Firefox
		\t3)	Safari
		""")
	sys.exit(0)

def search():
	# if no arguments are called, display a help menu
	if len(sys.argv) == 1:
		print("\nusage: profiler.py -u, --user [username]\n")
		sys.exit(1)

	# keep counter for sites found
	count = 0
	sites = manageSites()

	# keep list of sites found
	found_sites = []

	print(f"\nSearching for username: {arguments().user}\n")

	for url in sites:
		try:
			if arguments().timeout:
				time = int(arguments().timeout)
			else:
				time = int(8)
			
			if arguments().user_agent:
				agent = agents()

			else:
				agent = {
					"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
				}

			if arguments().allow_redirects:
				redirect = True
			else:
				redirect = False


			response = requests.get(url, timeout=time, headers=agent, allow_redirects=redirect)

			# If web server returns a good response, mark as found
			# Although, some sites will show a error page, technically returning
			# a 200 status code. False positives may happen.
			# Often to negate this, do not allow redirects
			if response.status_code == 200:
				print(f"[+][+] {url} \t>> FOUND")
				count += 1
				found_sites.append(url)
				# experimental, but allow user to use the open 
				# pages argument. Which will automatically open 
				# the found url pages for user. Warning, recommened
				# not to use on older systems.
				if arguments().open_pages:
					webbrowser.open_new_tab(url)
				# condition only called when using 
				# allow redirects argument
				if response.history:
					print("\t[\\][\\]Request was redirected,\
						\tmay be false positive!")
					print(f"\tRedirect: [/][/]{response.url}\n")

			else:
				print(f"[-][-] {url}")

		# if user cancels program
		except KeyboardInterrupt:
			print("\nUser cancelled search!\n")
			sys.exit(0)

		# if website times out or no internet connection is established
		except requests.exceptions.ConnectionError:
			print(f"[x][x] {url}")
			print("\tError: Failed to establish connection\n")
			pass 
		except requests.exceptions.ReadTimeout:
			print(f"[x][x] {url}")
			print("\tError: Request timed out!\n")
			pass

	#print(f"DEBUG: AGENT={agent}\n TIMEOUT={time}")

	print("\n\t\t\t-----------------")
	print(f"\t\t\t {count} results found!")
	print("\t\t\t-----------------\n")

	i = 1
	for found in found_sites:
		print(f"\t{i}) {found}")
		i += 1

	if arguments().write:
		if platform.system() == "Linux" or \
		platform.system() == "Darwin":
			# check if directory exists
			if not os.path.exists("/etc/profiler/"):
				os.mkdir("/etc/profiler/")

			file = f"/etc/profiler/profiler.{arguments().user}"

			f = open(file, "w")
			f.close()

			with open(file, "a") as f:
				for url in found_sites:
					f.write(url+"\n")

			print("\n\tFindings written to /etc/profiler/")

		elif platform.system() == "Windows":
			# write file to current path
			path = os.getcwd()

			file = f"{path}\\profiler.{arguments().user}"

			f = open(file, "w")
			f.close()

			with open(file, "a") as f:
				for url in found_sites:
					f.write(url+"\n")

			print(f"\n\tFindings written to {path}")


	print("\n")

	sys.exit(0)

if __name__ == "__main__":
	if arguments().version:
		version()
	elif arguments().list_agents:
		listAgents()
	else:
		search()
		
