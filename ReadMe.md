## Introduction

This script is used for uploading image and get markdown quote from file or clipboard (include screenshot) by simply click <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c/w</kbd> -> <kbd>ctrl</kbd>+<kbd>v</kbd>. Never worrying about copy image to markdown!

This script is based on [this](https://github.com/xzonepiece/markdown-img-upload-windows) implementation, which use [qiniu cloud](https://portal.qiniu.com/) as image storage and [AutoHotkey](http://www.ahkscript.org/) to get hot key action. For MAC users, an altertive implementation is [here](https://github.com/tiann/markdown-img-upload).

## Tools
* [Python](https://www.python.org)

> Require: `ConfigParser` modual.

* [AutoHotkey](http://ahkscript.org) + AutoHotkey.dll

> Install AutoHotkey from the official website and copy AutoHotkey.dll that match your system into **windows/System32** folder

* qiniu cloud account
Refer to [this](https://github.com/tiann/markdown-img-upload) repo to find out how to get AK, SK and url of your storage.

## Usage
### Settings
1. In `config.ini`, fill in your AK, SK, url and bucket.
2. Modify `upload_qiniu.ahk`. Set all the three path to the absolute path of your program.
3. Modify `clipboard.py`. Change the temporary store location of copied image to an **already exist path**.
4. Double click `upload_qiniu.ahk` to execute AutoHotkey script.

### Uploading from image file on the disk

> You can change the hot key settings in `upload_qiniu.ahk`.

1. Select an image file.
2. Click <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c</kbd>. A command window will show up.
3. After the command window disappear, the markdown script is in the clipboard and you can use <kbd>ctrl</kbd>+<kbd>v</kbd> to copy that to your markdown file.

### Uploading from screenshot and copied image.

1. You should first make the image in the clipboard, either use <kbd>ctrl</kbd>+<kbd>c</kbd> or right-click it and clike **Copy**. This process can automatically be done by most screenshot software.
2. Click <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>w</kbd>, again after the command window shows up and disappear, you can copy your markdown script.

Enjoy using **Markdown**!