;Add an icon for AutoHotKey task
Menu, Tray, Icon, D:\your\path\upload_folded.ico, ,1

; Upload image on qiniu cloud
^!c::
send, ^c
clipwait
;%comspec% stands for running in command line.
;Change the following path to the abs path of ```upload_qiniu.py```
Run %comspec%  /c "python D:\your\path\upload_qiniu.py %Clipboard%" /p
return
^!w::
;Change this as well!
Run %comspec%  /c "python D:\your\path\clipboard.py" /p
return