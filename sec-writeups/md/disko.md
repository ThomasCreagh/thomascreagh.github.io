# DISKO 1,2,3

---

this is a [pico ctf](https://picoctf.org/) challenge

---

#### Description

Q1:
> Can you find the flag in this disk image?
> Download the disk image [here](https://artifacts.picoctf.net/c/537/disko-1.dd.gz).

Q2:
> 
> 

Q3:
> 
> 

#### Disko 1
First thing I did was do `file disko-1.dd.gz` this gives me an idea of what I'm working with:
```
disko-1.dd.gz: gzip compressed data
was "disko-1.dd", last modified: Thu May 15 18:48:20 2025,
from Unix, original size modulo 2^32 52428800
```
This is a gunzip compressed file so I unzipped it with gunzip `gunzip disko-1.dd.gz`
then checked the file info agin `file disk-1.dd`
```
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2,
OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32,
heads 8, sectors 102400 (volumes > 32 MB), FAT (32 bit),
sectors/FAT 788, serial number 0x241a4420, unlabeled
```
When I looked inside the contents of the file it looked like it had some comprehensible text.
So I used the strings program and pipped that into grep to check for any strings with the word `pico` in the string:
```
$ strings disko-1.dd | grep "pico"

:/icons/appicon
# $Id: piconv,v 2.8 2016/08/04 03:15:58 dankogai Exp $
piconv -- iconv(1), reinvented in perl
  piconv [-f from_encoding] [-t to_encoding]
  piconv -l
  piconv -r encoding_alias
  piconv -h
B<piconv> is perl version of B<iconv>, a character encoding converter
a technology demonstrator for Perl 5.8.0, but you can use piconv in the
piconv converts the character encoding of either STDIN or files
Therefore, when both -f and -t are omitted, B<piconv> just acts
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
```
The flag printed right out of the command `picoCTF{1t5_ju5t_4_5tr1n9_be6031da}` was the correct flag.


#### Disko 2


