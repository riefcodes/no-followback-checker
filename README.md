# Instagram Non-Followback Checker

A simple Python script to find which Instagram accounts you follow that do not follow you back.

## Features

- Reads Instagram export JSON files
- Compares your `following` vs `followers`
- Prints accounts that do not follow you back
- Handles multiple Instagram JSON formats (`value`, `title`, or `href`)

## Project Structure

- `code.py` - Main script
- `following.json` - Exported following data from Instagram
- `followers_1.json` - Exported followers data from Instagram

## Requirements

- Python 3.8+

No external packages are required.

## How To Get Your Instagram Data

1. Open Instagram.
2. Go to **Settings** > **Accounts Center** > **Your information and permissions** > **Download your information**.
3. Request a download in **JSON** format.
4. Make sure the Date Range is **All Time**
5. After the export is ready, extract the ZIP file.
6. Copy these files into this project folder:
   - `following.json`
   - `followers_1.json`

Note: Depending on your Instagram export, follower files may be split (for example `followers_2.json`, `followers_3.json`, etc.). This project currently uses `followers_1.json`.

## Usage

Run this command in the project folder:

```bash
python code.py
```

## Example Output

```text
You are following 602 people.
219 people are following you.

There are 389 people who don't follow you back:

username_1
username_2
...
```

## Privacy Note

Your Instagram export files contain personal account data.

- Do not commit your real `following.json` and `followers_1.json` files to a public repository.
- Consider adding them to `.gitignore` before pushing to GitHub.
