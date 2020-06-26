<h1 align="center">
  <br>
  Get-Song
  <br>
</h1>

<h4 align="center">Script to retrieve the current playing song from spotify.</h4>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.8-blue.svg?style=for-the-badge" alt="Made with Python 3.8">
  </a>
</p>

# Overview

Get-Song is a small Python script used to retrieve the song a user is currently playing on spotify. It uses the Spotify API to get a token, that authorizes the user.

# Usage

As a refresh token is necessary for the Spotify API to function all the time, a request for the token has to be made first. The out-commented code opens a Spotify login screen, which redirects with a code used to verify the user.
After the code has been entered in the python console, a cURL request is printed, which returns a token and refresh token.
