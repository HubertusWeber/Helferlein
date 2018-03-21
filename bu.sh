#! /bin/sh
echo brew update
brew update
echo brew upgrade
brew upgrade
echo brew cleanup
brew cleanup
echo brew cask upgrade
brew cask upgrade
echo brew cask cleanup
brew cask cleanup
if [ $# -eq 1 ]
  then
  	echo updating tldr
  	tldr --update
  	echo updage/upgrade npm packages
  	npm up
	echo upgrade pip itself
	pip install --upgrade pip
	echo upgrade pip packages
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
fi