## monitorRegex
This was a small script I developed so I could get the earliest appointment as possible with my barber. I did this by using python's regex and requests module. The logic behind it is that it loops until 'NYE 30th' isn't found by the regex. Once it isn't in the html data a "Check for changes" message is sent via discord webhook.
