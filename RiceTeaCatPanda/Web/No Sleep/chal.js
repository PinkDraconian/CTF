var _0x1d8e = ['gamerfuel=Jan\x2027,\x202020\x2004:20:00', 'Jan\x2027,\x202020\x2004:20:00', 'getTime', 'exec', 'floor', 'getElementById', 'gamer\x20timer', 'AES', 'decrypt', 'U2FsdGVkX18kRm6FDkRVQfVuNPTxyOnJzpu8QnI/9UKoCXp6hQcley11nBnLIItj', 'ok\x20boomer', 'innerHTML', 'Utf8', 'cookie'];
(function (_0x29eed8, _0x4bb4aa) {
    var _0x47e29c = function (_0x2d3fd2) {
        while (--_0x2d3fd2) {
            _0x29eed8['push'](_0x29eed8['shift']());
        }
    };
    _0x47e29c(++_0x4bb4aa);
}(_0x1d8e, 0x99));
var toName = function (_0x545e19, _0x47cdd3) {
    _0x545e19 = _0x545e19 - 0x0;
    var _0x4275c2 = _0x1d8e[_0x545e19];
    return _0x4275c2;
};
document[toName('0x0')] = toName('0x1'); // document.getElementById == document['getElementById']
var countDownDate = new Date(toName('0x2'))[toName('0x3')]();
var x = setInterval(function () {
    var _0x27a8c6 = new Date(/[^=]*$/[toName('0x4')](document[toName('0x0')])[0x0])[toName('0x3')]();
    var _0x5b92f1 = new Date()['getTime']();
    var _0x3a5a33 = _0x27a8c6 - _0x5b92f1;
    var _0x4214a2 = Math[toName('0x5')](_0x3a5a33 / (0x3e8 * 0x3c * 0x3c * 0x18));
    var _0x48c0d9 = Math[toName('0x5')](_0x3a5a33 % (0x3e8 * 0x3c * 0x3c * 0x18) / (0x3e8 * 0x3c * 0x3c));
    var _0x2de271 = Math[toName('0x5')](_0x3a5a33 % (0x3e8 * 0x3c * 0x3c) / (0x3e8 * 0x3c));
    var _0x240ffb = Math['floor'](_0x3a5a33 % (0x3e8 * 0x3c) / 0x3e8);
    document[toName('0x6')](toName('0x7'))['innerHTML'] = _0x4214a2 + 'd\x20' + _0x48c0d9 + 'h\x20' + _0x2de271 + 'm\x20' + _0x240ffb + 's\x20';
    if (_0x3a5a33 < 0x0) {
        clearInterval(x);
        var decrypt = CryptoJS['AES']['decrypt']('U2FsdGVkX18kRm6FDkRVQfVuNPTxyOnJzpu8QnI/9UKoCXp6hQcley11nBnLIItj', 'ok boomer');
        document[toName('0x6')](toName('0x7'))[toName('0xc')] = decrypt['toString'](CryptoJS['enc'][toName('0xd')]);
    }
}, 0x3e8);
