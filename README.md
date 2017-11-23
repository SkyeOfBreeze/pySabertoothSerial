# python-sabertooth-serial
Unofficial python library for Synren/Sabertooth motor controllers via serial RS-232

# Compatible Sabertooth controllers
More or all that support serial may be compatible, but the list below shows what they are tested on. Feel free to notify me of other working devices by making a pull request to this file

- Sabertooth 2x25

# Platform

Python 2.7

# Tested Operating Systems

- Linux
- Windows

# How to install

## Linux

```
git clone https://github.com/btelman96/pySabertoothSerial.git
cd pySabertoothSerial
sudo python setup.py install
```

## Windows (Admin Only)

This assumes that both python and git are in PATH

```
git clone https://github.com/btelman96/pySabertoothSerial.git
cd pySabertoothSerial
python setup.py install
```

# How to use in other programs
Look at files in SabertoothSerial/examples/ to get an idea of how to use. Implementation of import may be different when trying to use in your own program.

If using linux, you need to make examples executable before attempting to run directly from source

```
chmod +x file-name.py
```

# Disclaimers
Dimension Engineering LLC. is not involved in this repo
