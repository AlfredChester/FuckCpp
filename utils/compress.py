import execjs

_jsFile = open('.\\js\\compress.js', 'r', encoding='u8')
_jsCompress = execjs.compile(
    _jsFile.read(), cwd='js\\node_modules'
)

def compress(src: str) -> str:
    return _jsCompress.call('compress', src)