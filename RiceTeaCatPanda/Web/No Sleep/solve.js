let CryptoJS = require("crypto-js");
let decrypt = CryptoJS['AES']['decrypt']('U2FsdGVkX18kRm6FDkRVQfVuNPTxyOnJzpu8QnI/9UKoCXp6hQcley11nBnLIItj', 'ok boomer');
console.log(decrypt['toString'](CryptoJS['enc']['Utf8']));
