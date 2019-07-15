#!/usr/bin/env python3

import argparse
import sys, os
import platform
import requests
import subprocess
import webbrowser
import datetime
from colorama import Fore, Style

# Clean the screen of the terminal 
def cleanScreen():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux" or "Darwin":
		subprocess.call(["clear"])
cleanScreen()

# Display title information
def title():
	print(Fore.RED + """


   _ (`-.  _  .-')                                              ('-.  _  .-')   
  ( (OO  )( \\( -O )                                           _(  OO)( \\( -O )  
 _.`     \\ ,------.  .-'),-----.    ,------.,-.-')  ,--.     (,------.,------.  
(__...--'' |   /`. '( OO'  .-.  '('-| _.---'|  |OO) |  |.-')  |  .---'|   /`. ' 
 |  /  | | |  /  | |/   |  | |  |(OO|(_\\    |  |  \\ |  | OO ) |  |    |  /  | | 
 |  |_.' | |  |_.' |\\_) |  |\\|  |/  |  '--. |  |(_/ |  |`-' |(|  '--. |  |_.' | 
 |  .___.' |  .  '.'  \\ |  | |  |\\_)|  .--',|  |_.'(|  '---.' |  .--' |  .  '.' 
 |  |      |  |\\  \\    `'  '-'  '  \\|  |_)(_|  |    |      |  |  `---.|  |\\  \\  
 `--'      `--' '--'     `-----'    `--'    `--'    `------'  `------'`--' '--' 

		\n\n""")

	print(Fore.GREEN + "\t\tWritten By: " + Fore.RED + "\tMatthew Greer")
	print(Fore.GREEN + "\t\tGithub: " + Fore.RED + "\thttps://github.com/DFC302")
	print(Fore.GREEN + "\t\tHTB: " + Fore.RED + "\t\thttps://www.hackthebox.eu/profile/17842")
	print(Style.RESET_ALL)

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
		help="Prompts webbrowser to open all found URL's.", 
		action="store_true")
	# change user agent
	parser.add_argument("-a", "--user-agent", 
		help="Change user agent.", 
		action="store")
	# List available agents
	parser.add_argument("-l", "--list-agents",
		help="List available user agents.",
		action="store_true")
	# List available sites
	parser.add_argument("-L", "--list-sites",
		help="List sites that profiler searches for users.",
		action="store_true")
	# Write results to file
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
		f"https://myspace.com/{arguments().user}", # Myspace # verify=False to pass SSL certificate
		f"https://www.pornhub.com/users/{arguments().user}", # Pornhub
		f"https://www.xvideos.com/profiles/{arguments().user}/", # Xvideos
		f"https://badoo.com/profile/{arguments().user}/", # Badoo
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
		f"https://profiles.wordpress.org/{arguments().user}", # Wordpress
		f"https://bitbucket.org/{arguments().user}/", # Bitbucket
		f"https://github.com/{arguments().user}", # Github
		f"https://{arguments().user}.blogspot.com/", # Blogspot
		f"https://www.etsy.com/people/{arguments().user}", # Etsy
		f"https://about.me/{arguments().user}", # About me
		f"https://imgur.com/user/{arguments().user}", # imgur
		f"http://{arguments().user}.tumblr.com", # tumblr
		f"https://foursquare.com/{arguments().user}", # foursquare
		f"https://mix.com/{arguments().user}", # Mix / StumbleUpon
		f"https://www.reverbnation.com/{arguments().user}", # Reverb Nation
		f"http://us.viadeo.com/en/profile/{arguments().user}", # Viadeo
		f"https://www.gaia.com/person/{arguments().user}", # gaia
		f"https://weheartit.com/{arguments().user}", # We Heart it
		f"https://www.deviantart.com/{arguments().user}", # Deviant art
		f"https://www.flickr.com/photos/{arguments().user}", # Flickr
		f"https://www.quora.com/profile/{arguments().user}", # Quora
		f"https://www.reverbnation.com/{arguments().user}/", # Reverb nation
		f"https://imageshack.us/user/{arguments().user}", # Imageshack
		f"https://{arguments().user}.livejournal.com", # Live journal
		f"https://www.zillow.com/profile/{arguments().user}/", # Zillow
		f"https://photobucket.com/user/{arguments().user}/profile", # Photobucket, needs redirect on
		f"https://www.tripadvisor.com/Profile/{arguments().user}", #Trip Advisor
		f"https://www.linkedin.com/in/{arguments().user}/", #LinkedIn
		f"https://plus.google.com/+{arguments().user}", #Google Plus
		f"https://venmo.com/{arguments().user}", #Venmo
		f"https://poshmark.com/closet/{arguments().user}", #Poshmark
		f"https://ello.co/{arguments().user}", #Ello
		f"https://www.quora.com/profile/{arguments().user}",#Quora
		f"https://www.periscope.tv/{arguments().user}/", #Periscope
		f"https://medium.com/{arguments().user}", #Medium
		f"https://www.viewbug.com/member/{arguments().user}", # Viewbug
		f"https://vsco.co/{arguments().user}/images/1", # Vsco
		f"https://www.girlsaskguys.com/user/{arguments().user}", # Girls ask Guys
		f"https://cash.me/{arguments().user}", #cash me page
		f"https://about.me/{arguments().user}", # about me 
		f"https://www.paypal.me/{arguments().user}", # paypal
		f"https://quizlet.com/{arguments().user}", # quizlet 
		f"https://www.myfitnesspal.com/{arguments().user}", # myfitnesspal
	]

	return sites

# Used to display list of avaialble sites
def listOfSites():
	title()

	sites = [
		"Instagram",
		"Facebook",
		"Twitter",
		"Pinterest",
		"Myspace (verify=False to pass SSL certificate)",
		"Pornhub",
		"Xvideos",
		"Badoo",
		"Reddit",
		"Youtube",
		"askfm",
		"spotify",
		"Soundcloud",
		"XBOX",
		"Playstation",
		"Wordpress",
		"Delaware Technical Community College",
		"Wordpress",
		"Bitbucket",
		"Github",
		"Blogspot",
		"Etsy",
		"About me",
		"imgur",
		"tumblr",
		"foursquare",
		"Mix / StumbleUpon",
		"Reverb Nation",
		"Viadeo",
		"gaia",
		"We Heart it",
		"Deviant art",
		"Flickr",
		"Quora",
		"Reverb nation",
		"Imageshack",
		"Live journal",
		"Zillow",
		"Photobucket (needs redirect on)",
		"Trip Advisor",
		"LinkedIn",
		"Google Plus",
		"fVenmo",
		"Poshmark",
		"Ello",
		"Quora",
		"Periscope",
		"Medium",
		"Viewbug",
		"Vsco",
		"Girls ask Guys",
		"cash me",
		"about me", 
		"paypal",
		"quizlet",
		"myfitnesspal",
	]

	print(f"\t\t{Fore.RED}List Of Sites{Style.RESET_ALL}")
	print(f"\t\t{Fore.RED}============={Style.RESET_ALL}\n")

	i = 1
	for site in sites:
		print(f"\t\t{i})\t{site}")
		i+=1

	print("\n")

# Display version information
def version():
	title()
	
	print(Fore.GREEN + "\t\tVersion:" + Fore.RED + "\t3.0")

	print()

# Change header in request
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

# list available agents that can be used
def listAgents():
	title()

	print(f"""{Fore.RED}
		User-Agents {Style.RESET_ALL}
	       -------------
		1)	Chrome
		2)	Firefox
		3)	Safari
		""")
	sys.exit(0)

# search sites for defined user
# option arguments logically set
def search():
	# display title
	title()

	# if no arguments are called, display a help menu
	if len(sys.argv) == 1:
		print("Missing arguments!\n")
		sys.exit(1)

	# keep counter for sites found
	count = 0
	sites = manageSites()

	# keep list of sites found
	found_sites = []

	print(f"\nSEARCHING FOR USERNAME: {Fore.YELLOW}{arguments().user}{Style.RESET_ALL}\n")

	for url in sites:
		try:
			if arguments().timeout: # if timeout is specified by user, set it
				time = int(arguments().timeout)
			else:
				time = int(5) # default request timeout
			
			if arguments().user_agent: # If user agent is chosen by user, set it
				agent = agents()

			else:
				agent = { # default user agent
					"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
				}

			if arguments().allow_redirects: # if redirects are to be used
				redirect = True
			else:
				redirect = False # default set to not allow redirects

			# Myspace does not work well with certifications with requets
			# If myspace is being used, verfiy cert is set to fale
			# else, all others are set to default of true
			if "https://myspace.com/" in url:
				from requests.packages.urllib3.exceptions import InsecureRequestWarning
				requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
				response = requests.get(url, timeout=time, headers=agent, allow_redirects=redirect, verify=False)
			else:
				response = requests.get(url, timeout=time, headers=agent, allow_redirects=redirect)

			# If web server returns a good response, mark as found
			# Although, some sites will show a error page, technically returning
			# a 200 status code. False positives may happen.
			# Often to negate this, do not allow redirects
			if response.status_code == 200:
				#print(f"{Fore.YELLOW}[+][+]{Style.RESET_ALL} {url} \t>> {Fore.YELLOW}FOUND{Style.RESET_ALL}")
				print(f"{Fore.YELLOW}[+][+] {url} {Style.RESET_ALL}")
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

	# DEBUG AGENT AND TIMEOUT IF NEEDED
	#print(f"DEBUG: AGENT={agent}\n TIMEOUT={time}")

	print("\n\t\t\t-------------------------")
	print(f"\t\t\t {Fore.YELLOW}!!-- {Style.RESET_ALL}{Fore.RED}{count} results found{Style.RESET_ALL}{Fore.YELLOW} -!!{Style.RESET_ALL}")
	print("\t\t\t-------------------------\n")

	# add increment for found sites
	i = 1
	for found in found_sites:
		print(f"\t{Fore.YELLOW}{i}) {found}")

		i += 1

		Style.RESET_ALL

	# write to file if user chooses
	if arguments().write:
		now = datetime.datetime.now() # use current date and time

		if platform.system() == "Linux" or \
		platform.system() == "Darwin": # for linux or mac
			path = os.getcwd()

			file = f"{path}/profiler.{arguments().user}"
			f = open(file, "w")
			f.close()

			with open(file, "a") as f:
				f.write(str(now) + "\n")

				for url in found_sites:
					f.write(url+"\n")

			print(f"\n\tFindings written to /etc/profiler/ @ {now}")

		elif platform.system() == "Windows":
			# write file to current path
			path = os.getcwd()

			file = f"{path}\\profiler.{arguments().user}"

			f = open(file, "w")
			f.close()

			with open(file, "a") as f:
				f.write(str(now) + "\n")

				for url in found_sites:
					f.write(url+"\n")

			print(f"\n\tFindings written to {path} @ {now}")


	print("\n")

	sys.exit(0)

if __name__ == "__main__":
	if arguments().version: # display version
		version()
	elif arguments().list_agents: # display list of agents
		listAgents()
	elif arguments().list_sites: # display list of sites
		listOfSites()
	else:
		search() # else search
		
