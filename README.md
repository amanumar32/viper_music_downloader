# **Viper Music Downloader**
#### **v1.0.1**

## **What's New?**

- **ANSI Escape Codes:** New ANSI Escape Codes for a prettier and more decorative console print.
- **Inline Commands:** Support for editing settings through inline commands, similar to `/exit`. Command menu available on load.
- **Bugs:** Minor bug fixes.

## **Introduction**

_Viper Music Downloader_ is a simple but robust Python application that takes a search parameter from input and downloads it to your local storage. The search parameter can be a query or YouTube video URL. You can specify the default media type, download path, quality and other settings in [settings.json](./settings.json).

## **Requirements**

- **Python:** The Python Runtime must be installed on your device. If you don't already have Python installed, download and install it from [the official website](https://python.org).
- **Internet:** A stable internet connection is required to install the required Python packages and download the songs.

## **Settings**

You can modify these settings fields with these data type to suit your need:

- **default_download_path:** Specifies the default download path for all media. Can contain a path in relative `string` (_e.g. ./downloads_) or an absolute path (_e.g. C:\Users\Public\Videos_).
- **download_quality:** Specifies the download quality. It can contain an `integer` between `1` and `3`. _1_ represents the lowest quality and _3_ the highest.
- **default_media_type:** Specifies the media type. Can be either `audio` or `video`.
- **always_overwrite_similar_files:** Specifies whether a newly downloaded file with a similar filename with an existing file overwrites that file or not. It's value should be a `boolean`.

## **Running**

To run the code, double click the [viper.bat](./viper.bat) file and follow the on screen prompts to download your media.

#### **[The Cyan Empire](https://the-cyan-empire.netlify.app)**