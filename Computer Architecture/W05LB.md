# Comp Arch - Procedures (cont'd)

> 2017/09/21


<!-- vim-markdown-toc GFM -->
* [Data Directives](#data-directives)

<!-- vim-markdown-toc -->

- Understand fibonacci MIPS

## Data Directives

- .BYTE
- .WORD
- ...
- Sets aside storage in memory for a var
- Syntax
	- ...
- Examples:
```asm
.DATA
var1:	.BYTE	'A', 'E', 127, -1, '\n'
var2:	.HALF	-10, 0xffff
var3:	.WORD	0x12345678:100
var4:	.FLOAT	12.3, -0.1
var5:	.DOUBLE	1.5e-10
array:	.SPACE	100
str1:	.ASCII	"A string"
str1	.ASCIIZ	"A null-terminated string"
```

