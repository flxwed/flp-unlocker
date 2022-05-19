# flp-unlocker
Allows you to reopen FLPs saved in the FL Studio trial.

<br>

## How to use it
You will need any version of Python 3. You can install one [here](https://www.python.org/downloads/).

Once you've installed python, run the script with the file you want to unlock in the arguments. The script will automatically save a backup for you, as the unlock process is irreversible. **Do not delete this until you know the FLP functions correctly!**

> Note: Some FL plugins will not work when using an unlocked flp. Try to find and avoid plugins like these as most of them will delete your settings entirely when this happens.

```bash
> py flpunlocker.py "C:/Users/Bob/Desktop/My FLP.flp"
making backup...
saved to MyFLP.flp.bak

unlocking...
flp unlocked successfully.
```

I personally also have this program [added to my right click context menu](https://www.wikihow.com/Add-New-Options-to-Right-Click-Menu-in-Windows) for convenience. **Do not attempt this unless you know what you are doing. This process involves editing the registry.**

<br>

## How it works
By default, if a file is saved in the trial version of FL studio, attempting to reopen this file with another trial version fails. Files saved in paid versions of FL studio trial seem to have a slightly modified header and a string of bytes not present in files saved in trial versions, making it openable by anyone, *even trial users*.

With this knowledge, comparing a trial version file to a paid version file in [hexed.it](https://hexed.it), the following bytes seem to be present:

![image](https://user-images.githubusercontent.com/29684696/264918285-136b02f2-53be-42aa-815f-43b35ae928c4.png)

Notice that there is an additional string of 44 bytes not present in a trial version file. To replicate this in hexedit simply right click the blue cell and add 44 bytes.

<br>

## Notice
This code has not been updated in a long time. I am publishing the project to allow others to recieve the same value from this script as I did.

If this code does not function, either at all or for a specific version, feel free to [open an issue](https://github.com/flxwed/flp-unlocker/issues/new) and I'll try to fix it for you if I'm still around.
