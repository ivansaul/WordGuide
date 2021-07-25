# Notes
## Windows
### Release v0.1
- Compile with `auto-py-to-exe`
    ```
    pip install auto-py-to-exe==2.9.0
    ```
- Downgrade PyInstaller to 4.3
    ```
    pip install PyInstaller==4.3
    ```
- Add all `dlls` in `root dir (.)`
- In advanced settings `--collect-submodules ffpyplayer`

## Linux
### Release v0.1
- Compile with `cx_Freeze`
    ```bash
    pip install cx-Freeze==6.7
    ```
- Run    
    ```bash
    python setup.py build
    ```