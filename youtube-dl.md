**Download Audio Only**

1. Get the list of streams

```powershell
youtube-dl -F <url>
```

2. Choose the correct format usually 140 like so:

   ```powershell
   youtube-dl -f 140 <url>
   ```

   done

   ### Add playlist numbers
   
   ```powershell
   youtube-dl -o "%(playlist_index)s-%(title)s.%(ext)s" <playlist_link>
   ```
   
   