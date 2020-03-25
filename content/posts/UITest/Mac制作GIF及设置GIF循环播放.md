---
title: 'MAC制作GIF及设置GIF循环播放'
tags:
  - GIF
categories:
  - Tool
date: 2016-11-23 16:20:00
---

>需求：在Mac电脑中录制操作，并生成GIF文件。GIF文件需要循环播放。

## 工具选择
- [Recordit](http://recordit.co/)，7.2M大小，Free
- [gifsicle](http://www.lcdf.org/gifsicle/)，`加工`GIF图片工具

<!--more-->

## 安装Recordit，录制GIF图片

- [下载最新版本](http://recordit.co/latest-osx)，解压后直接运行
- 点击Record，会提示选择录制范围
- 选择范围后，再点击Recordit的图标，开始录制
- `操作`完成后，再点击Recordit的图标，录制结束
>Recordit会将本次的录制内容上传至`服务器`，如果需要删除时，需要`手动`在Recordit中删除

## 使用gifsicle设置图片为循环播放

- 下载gifsicle，[gifsicle-1.88.tar.gz](http://www.lcdf.org/gifsicle/gifsicle-1.88.tar.gz)，解压
- `Terminal`进入解压目录，运行`./configure --disable-gifview --disable-gifdiff`
```
➜  gifsicle-1.88 ./configure --disable-gifview --disable-gifdiff
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make sets $(MAKE)... (cached) yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking how to run the C preprocessor... gcc -E
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for random... yes
checking for strerror... yes
checking for strtoul... yes
checking for mkstemp... yes
checking for library containing pow... none required
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking for inttypes.h... (cached) yes
checking for unistd.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for sys/types.h... (cached) yes
checking for uintptr_t... yes
checking for int64_t... yes
checking size of unsigned int... 4
checking size of unsigned long... 8
checking size of void *... 8
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating config.h
config.status: executing depfiles commands
```
- 执行`make`命令
```
➜  gifsicle-1.88 make
/Library/Developer/CommandLineTools/usr/bin/make  all-recursive
Making all in src
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT clp.o -MD -MP -MF .deps/clp.Tpo -c -o clp.o clp.c
mv -f .deps/clp.Tpo .deps/clp.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT fmalloc.o -MD -MP -MF .deps/fmalloc.Tpo -c -o fmalloc.o fmalloc.c
mv -f .deps/fmalloc.Tpo .deps/fmalloc.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT giffunc.o -MD -MP -MF .deps/giffunc.Tpo -c -o giffunc.o giffunc.c
mv -f .deps/giffunc.Tpo .deps/giffunc.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT gifread.o -MD -MP -MF .deps/gifread.Tpo -c -o gifread.o gifread.c
mv -f .deps/gifread.Tpo .deps/gifread.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT gifunopt.o -MD -MP -MF .deps/gifunopt.Tpo -c -o gifunopt.o gifunopt.c
mv -f .deps/gifunopt.Tpo .deps/gifunopt.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT merge.o -MD -MP -MF .deps/merge.Tpo -c -o merge.o merge.c
mv -f .deps/merge.Tpo .deps/merge.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT optimize.o -MD -MP -MF .deps/optimize.Tpo -c -o optimize.o optimize.c
mv -f .deps/optimize.Tpo .deps/optimize.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT quantize.o -MD -MP -MF .deps/quantize.Tpo -c -o quantize.o quantize.c
mv -f .deps/quantize.Tpo .deps/quantize.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT support.o -MD -MP -MF .deps/support.Tpo -c -o support.o support.c
mv -f .deps/support.Tpo .deps/support.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT xform.o -MD -MP -MF .deps/xform.Tpo -c -o xform.o xform.c
mv -f .deps/xform.Tpo .deps/xform.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT gifsicle.o -MD -MP -MF .deps/gifsicle.Tpo -c -o gifsicle.o gifsicle.c
gifsicle.c:24:9: warning: 'static_assert' macro redefined [-Wmacro-redefined]
#define static_assert(x, msg) switch ((int) (x)) case 0: case !!((int) (x)):
        ^
/usr/include/assert.h:107:9: note: previous definition is here
#define static_assert _Static_assert
        ^
1 warning generated.
mv -f .deps/gifsicle.Tpo .deps/gifsicle.Po
gcc -DHAVE_CONFIG_H -I. -I..    -I../include   -g -O2 -MT gifwrite.o -MD -MP -MF .deps/gifwrite.Tpo -c -o gifwrite.o gifwrite.c
mv -f .deps/gifwrite.Tpo .deps/gifwrite.Po
gcc  -g -O2   -o gifsicle clp.o fmalloc.o giffunc.o gifread.o gifunopt.o merge.o optimize.o quantize.o support.o xform.o gifsicle.o  gifwrite.o
make[2]: Nothing to be done for `all-am'.
```
- 进入`src`目录，将原`GIf`图片(目录:`~/Documents/test.gif`)设置为循环播放
```
➜  gifsicle-1.88 cd src
➜  src ./gifsicle -bl ~/Documents/test.gif
```

> 将GIF图片设置为`循环播放`已完成。

- 其它`gifsicle`参数

```
'Gifsicle' manipulates GIF images. Its most common uses include combining
single images into animations, adding transparency, optimizing animations for
space, and printing information about GIFs.

Usage: gifsicle [OPTION | FILE | FRAME]...

Mode options: at most one, before any filenames.
  -m, --merge                   Merge mode: combine inputs, write stdout.
  -b, --batch                   Batch mode: modify inputs, write back to
                                same filenames.
  -e, --explode                 Explode mode: write N files for each input,
                                one per frame, to 'input.frame-number'.
  -E, --explode-by-name         Explode mode, but write 'input.name'.

General options: Also --no-OPTION for info and verbose.
  -I, --info                    Print info about input GIFs. Two -I's means
                                normal output is not suppressed.
      --color-info, --cinfo     --info plus colormap details.
      --extension-info, --xinfo --info plus extension details.
      --size-info, --sinfo      --info plus compression information.
  -V, --verbose                 Prints progress information.
  -h, --help                    Print this message and exit.
      --version                 Print version number and exit.
  -o, --output FILE             Write output to FILE.
  -w, --no-warnings             Don't report warnings.
      --no-ignore-errors        Quit on very erroneous input GIFs.
      --conserve-memory         Conserve memory at the expense of speed.
      --multifile               Support concatenated GIF files.

Frame selections:               #num, #num1-num2, #num1-, #name

Frame change options:
  --delete FRAMES               Delete FRAMES from input.
  --insert-before FRAME GIFS    Insert GIFS before FRAMES in input.
  --append GIFS                 Append GIFS to input.
  --replace FRAMES GIFS         Replace FRAMES with GIFS in input.
  --done                        Done with frame changes.

Image options: Also --no-OPTION and --same-OPTION.
  -B, --background COL          Make COL the background color.
      --crop X,Y+WxH, --crop X,Y-X2,Y2
                                Crop the image.
      --crop-transparency       Crop transparent borders off the image.
      --flip-horizontal, --flip-vertical
                                Flip the image.
  -i, --interlace               Turn on interlacing.
  -S, --logical-screen WxH      Set logical screen to WxH.
  -p, --position X,Y            Set frame position to (X,Y).
      --rotate-90, --rotate-180, --rotate-270, --no-rotate
                                Rotate the image.
  -t, --transparent COL         Make COL transparent.

Extension options:
      --app-extension N D       Add an app extension named N with data D.
  -c, --comment TEXT            Add a comment before the next frame.
      --extension N D           Add an extension number N with data D.
  -n, --name TEXT               Set next frame's name.
      --no-comments, --no-names, --no-extensions
                                Remove comments (names, extensions) from input.
Animation options: Also --no-OPTION and --same-OPTION.
  -d, --delay TIME              Set frame delay to TIME (in 1/100sec).
  -D, --disposal METHOD         Set frame disposal to METHOD.
  -l, --loopcount[=N]           Set loop extension to N (default forever).
  -O, --optimize[=LEVEL]        Optimize output GIFs.
  -U, --unoptimize              Unoptimize input GIFs.

Whole-GIF options: Also --no-OPTION.
      --careful                 Write larger GIFs that avoid bugs in other
                                programs.
      --change-color COL1 COL2  Change COL1 to COL2 throughout.
  -k, --colors N                Reduce the number of colors to N.
      --color-method METHOD     Set method for choosing reduced colors.
  -f, --dither                  Dither image after changing colormap.
      --gamma G                 Set gamma for color reduction [2.2].
      --resize WxH              Resize the output GIF to WxH.
      --resize-width W          Resize to width W and proportional height.
      --resize-height H         Resize to height H and proportional width.
      --resize-fit WxH          Resize if necessary to fit within WxH.
      --scale XFACTOR[xYFACTOR] Scale the output GIF by XFACTORxYFACTOR.
      --resize-method METHOD    Set resizing method.
      --resize-colors N         Resize can add new colors up to N.
      --transform-colormap CMD  Transform each output colormap by shell CMD.
      --use-colormap CMAP       Set output GIF's colormap to CMAP, which can
                                be 'web', 'gray', 'bw', or a GIF file.
```

## 总结

- 使用MAC录制GIF图片，只需要Recordit就可以
- 使用`gifsicle`处理图片
  - 将图片转为GIF
  - 处理GIF的机制，循环次数、设置大小、透明度等
