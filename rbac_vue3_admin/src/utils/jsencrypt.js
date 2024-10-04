import JSEncrypt from 'jsencrypt/bin/jsencrypt.min'


const publicKey = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMMVoaq5RKxllJjQ/7osuAX3ofZOMkWi\n'+
'72eesqwbzzBqfLkC9War/CxxDiepo7E9MMV8XbW0STd54hTQCLMVfJUCAwEAAQ=='  

const privateKey = 'MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAwxWhqrlErGWUmND/\n'+
'uiy4Bfeh9k4yRaLvZ56yrBvPMGp8uQL1Zqv8LHEOJ6mjsT0wxXxdtbRJN3niFNAI\n'+
'sxV8lQIDAQABAkEAhKzCfVRw4vpWvDNvqBNfuBc5HEUEJZ3xSbyBcVGccCTbTjOS\n'+
'dpjpt0VgNBCRrLDPYB1Vhtd1xzjkRJQuJLQawQIhAO29JY2dmp8eFpjjvlndFm+c\n'+
'+ucK0eOSftwd1wve9opFAiEA0hG8xCXjgpth3Vlfd3Lxcoc1Zws2Cz8+yi0qxPX4\n'+
'9hECIGPtnEpRU7vMLt1m5QzqxFJ33nKc9qo8Wnx1Qn3n4yMtAiEAoLuDpM2cy9Va\n'+
'R0RYAIyJY+lCmiqA2pA02fs/S18tdBECIB8gPcEkMNB18GV6YgEl7udzgtM+QPsQ\n'+
'PsCZSkCdxWaC'

export function encrypt(txt) {
  const encryptor = new JSEncrypt()
  encryptor.setPublicKey(publicKey) 
  return encryptor.encrypt(txt)
}

export function decrypt(txt) {
  const encryptor = new JSEncrypt()
  encryptor.setPrivateKey(privateKey)
  return encryptor.decrypt(txt)
}

