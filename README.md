# Auto-Join-Online-Meetings

Python program to auto join your online meetings be it for schools, colleges or professional meetings based on the schedule provided to the program.

## Features

- Add meeting information in the meetingInfo python file
- Auto joins and leaves the meeting based on information fed

## Modules Used

Following are the modules and their corresponding documentaion links that are being used.
| Module | Documentation Link |
| ------ | ------ |
| webbrowser | https://docs.python.org/3/library/webbrowser.html |
| datetime | https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime |
| time | https://docs.python.org/3/library/time.html?highlight=time#module-time |
| pytautogui | https://pyautogui.readthedocs.io/en/latest/ |

## How To Run
First, install pyautogui:

```sh
pip install pyautogui
```
Then feed meeting information in meetingInfo file in the specified format:
```sh
["meetingLink", "startTime(24hr format)", "endTime(24hr format)"]
```
Then run the python program:

```sh
python mainCode.py
```

## Future Work
- Sort the meetings information list according to the meeting's starting time
- Extract meetings information from an Excel file (that contains the schedule of meetings)
- Currently it works for Zoom only, so different platforms like Cisco, Google Meet, etc. will also be included

## Note

This repo is only for educational purpose, don't misuse it for bunking classes or office meetings.
(Just kidding)
