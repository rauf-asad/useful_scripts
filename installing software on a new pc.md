You dont need to install any software before you do this

Open powershell as administrator by searching for it in windows

Then type the following and press enter:

```powershell
Set-ExecutionPolicy AllSigned
```

Then the following in one go (copy the whole block below and press enter):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

After that once this is executed, run this in the same place:

```powershell
refreshenv
```

Run:

```powershell
choco feature enable -n allowGlobalConfirmation
```

now run:

```powershell
choco install googlechrome vlc firefox 7zip.install skype teamviewer python ffmpeg handbrake.install utorrent vscode.install zoom
```

now every once in a while run the following command to update all your software:

```powershell
choco upgrade all
```