<!DOCTYPE html>
<html>
<head>
  <title>Online RSA Key Generator</title>
  <!--  <base id="basetag" href="/jsencrypt/"> -->
  <!--[if IE]>
  <script type='text/javascript'>
    (function() {
      var tag = document.getElementById('basetag');
      tag.href = location.protocol + '//' + location.host + '/jsencrypt/';
    }());
  </script>
  <![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
  <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="bin/jsencrypt.js"></script>
  <script type="text/javascript" src="bin/FileSaver.js"></script>
  <script type="text/javascript" src="bin/crypto.js/components/core.js"></script>
  <script type="text/javascript" src="bin/crypto.js/rollups/aes.js"></script>
  <script type="text/javascript" src="bin/crypto.js/components/enc-base64-min.js"></script>
  <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-450670-2']);
    _gaq.push(['_trackPageview']);
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
  </script>
  <link href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet" type="text/css">
</head>
<body>
<nav class="navbar navbar-inverse" role="navigation">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">JSEncrypt</a>
    </div>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li >
          <a href="index.html">Home</a>
        </li>
        <li >
          <a href="demo/index.html">Demo</a>
        </li>
        <li >
          <a href="test/index.html">Test</a>
        </li>
        <li>
          <a href="https://github.com/travist/jsencrypt/archive/master.zip" role="button">Download</a>
        </li>
        <li>
          <a href="https://github.com/travist/jsencrypt" role="button">GitHub Project</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<div class="container">
  <div class="row">
  <div class="panel panel-default">
    <div class="panel-heading"><h1>Online RSA Key Generator</h1></div>
    <div class="panel-body">
      <div class="row col-lg-12">
        <div class="well">
          <!-- frontpage banner -->
          <ins class="adsbygoogle"
               style="display:inline-block;width:728px;height:90px"
               data-ad-client="ca-pub-1902035200208763"
               data-ad-slot="9043467163"></ins>
          <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
          </script>
        </div>
      </div>
      <div class="col-lg-2">
        <div class="btn-group">
          <div class="input-group">
            <span class="input-group-addon">Key Size</span>
            <button class="btn btn-default dropdown-toggle" id="key-size" type="button" data-value="1024"
                    data-toggle="dropdown">1024 bit <span class="caret"></span></button>
            <ul class="dropdown-menu">
              <li><a class="change-key-size" data-value="512" href="#">512 bit</a></li>
              <li><a class="change-key-size" data-value="1024" href="#">1024 bit</a></li>
              <li><a class="change-key-size" data-value="2048" href="#">2048 bit</a></li>
              <li><a class="change-key-size" data-value="4096" href="#">4096 bit</a></li>
            </ul>
          </div>
        </div>
        <br>&nbsp;<br>
        <button id="generate" class="btn btn-primary">Generate New Keys</button>
        <br>&nbsp;<br>
        <span><i><small id="time-report"></small></i></span>
        <br>&nbsp;<br>
        <label for="async-ck"><input id="async-ck" type="checkbox"> Async</label>
        <br>&nbsp;<br>
        <button id="dlkey" class="btn btn-primary">Download Private Key</button>
      </div>
      <div class="col-lg-10">
        <div class="row">
          <div class="col-lg-6">
            <label for="privkey">Private Key</label><br/>
            <small>
              <textarea id="privkey" rows="15" style="width:100%"></textarea>
            </small>
          </div>
          <div class="col-lg-6">
            <label for="pubkey">Public Key</label><br/>
            <small><textarea id="pubkey" rows="15" style="width:100%" readonly="readonly"></textarea></small>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="row">
  <div class="panel panel-default">
    <div class="panel-heading"><h3>RSA Encryption Test</h3></div>
    <div class="panel-body">
      <div class="col-lg-5">
        <label for="input">Text to encrypt:</label><br/>
        <textarea id="input" name="input" style="width: 100%" rows="4">This is a test!</textarea>
      </div>
      <div class="col-lg-2">
        <label>&nbsp;</label><br/>
        <button id="execute" class="btn btn-primary">Encrypt / Decrypt</button>
      </div>
      <div class="col-lg-5">
        <label for="crypted">Encrypted:</label><br/>
        <textarea id="crypted" name="crypted" style="width: 100%" rows="4"></textarea>
      </div>
    </div>
  </div>
</div>
<script type="text/javascript">
  $(function () {

    //Change the key size value for new keys
    $(".change-key-size").each(function (index, value) {
      var el = $(value);
      var keySize = el.attr('data-value');
      el.click(function (e) {
        var button = $('#key-size');
        button.attr('data-value', keySize);
        button.html(keySize + ' bit <span class="caret"></span>');
        e.preventDefault();
      });
    });

    // Execute when they click the button.
    $('#execute').click(function () {

      // Create the encryption object.
//      var crypt = new JSEncrypt();
//      var crypt = encrypt;

      // Set the private.
//      crypt.setPrivateKey($('#privkey').val());
//      //return;
//      // If no public key is set then set it here...
//      var pubkey = $('#pubkey').val();
//      if (!pubkey) {
//        $('#pubkey').val(crypt(.getPublicKey());
//      }

      // Get the input and crypted values.
      var input = $('#input').val();
      var crypted = $('#crypted').val();

      // Alternate the values.
      if (input) {
        $('#crypted').val(JSON.stringify(encrypt(input)));
        $('#input').val('');
      }
      else if (crypted) {
        var cryp = JSON.parse(crypted);
        var decrypted = decrypt(cryp['encryptedKey'],cryp['encryptedMessage'])
        if (!decrypted)
          decrypted = 'Error?';
        $('#input').val(decrypted);
        $('#crypted').val('');
      }
    });

    var generateKeys = function () {
      var sKeySize = $('#key-size').attr('data-value');
      var keySize = parseInt(sKeySize);
      var crypt = new JSEncrypt({default_key_size: keySize});
      var async = $('#async-ck').is(':checked');
      var dt = new Date();
      var time = -(dt.getTime());
      if (async) {
        $('#time-report').text('.');
        var load = setInterval(function () {
          var text = $('#time-report').text();
          $('#time-report').text(text + '.');
        }, 500);
        crypt.getKey(function () {
          clearInterval(load);
          dt = new Date();
          time += (dt.getTime());
          $('#time-report').text('Generated in ' + time + ' ms');
          $('#privkey').val(crypt.getPrivateKey());
          $('#pubkey').val(crypt.getPublicKey());
        });
        return;
      }
      crypt.getKey();
      dt = new Date();
      time += (dt.getTime());
      $('#time-report').text('Generated in ' + time + ' ms');
      $('#privkey').val(crypt.getPrivateKey());
      $('#pubkey').val(crypt.getPublicKey());
    };

    var downloadKey = function () {
      var privKey = $('#privkey').val();
      var blob = new Blob([privKey], {type: "text/plain;charset=utf-8"});
      saveAs(blob, "privatekey.rsa");
    }

    // If they wish to generate new keys.
    $('#generate').click(generateKeys);
    $('#dlkey').click(downloadKey);
    generateKeys();

    // code below from https://medium.com/@tikiatua/symmetric-and-asymmetric-encryption-with-javascript-and-go-240043e56daf

    // define the characters to pick from
    var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz*&-%/!?*+=()";
    // create a key for symmetric encryption
    // pass in the desired length of your key
    var genRandomString = function genRandomString(keyLength){
      var randomstring = '';

      for (var i=0; i < keyLength; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstring += chars.substring(rnum,rnum+1);
      }
      return randomstring;
    };

    // encrypt a javascript object into a payload to be sent
    // to a server or stored on the client
    var encrypt = function encrypt(data) {

      var publicKey = $('#pubkey').val();
      // Create a new encryption key (with a specified length)
      var key = genRandomString(50);
      // convert data to a json string
      var dataAsString = JSON.stringify(data);
      // encrypt the data symmetrically 
      // (the cryptojs library will generate its own 256bit key!!)
      var aesEncrypted = CryptoJS.AES.encrypt(dataAsString, key);
      // get the symmetric key and initialization vector from
      // (hex encoded) and concatenate them into one string
      var aesKey = JSON.stringify({
//        key : String(aesEncrypted.key),
        key : String(key),
        iv : String(aesEncrypted.iv)
      });
      // the data is base64 encoded 
      var encryptedMessage = aesEncrypted.toString();

      // we create a new JSEncrypt object for rsa encryption
      var rsaEncrypt = new JSEncrypt();

      // we set the public key (which we passed into the function)
      rsaEncrypt.setPublicKey(publicKey);
      // now we encrypt the key & iv with our public key
      var encryptedKey = rsaEncrypt.encrypt(aesKey);
      // and concatenate our payload message
      var payload = {
        encryptedKey: encryptedKey,
        encryptedMessage: encryptedMessage
      };

      return payload;
    };

    var decrypt = function decrypt(encryptedKey, encryptedData) {
      var rsaDecrypt = new JSEncrypt();
      var privateKey = $('#privkey').val();
      rsaDecrypt.setPrivateKey(privateKey);
      var aeskey = JSON.parse(rsaDecrypt.decrypt(encryptedKey));
      return JSON.parse(CryptoJS.AES.decrypt(encryptedData, aeskey['key']).toString(CryptoJS.enc.Utf8));
    }

  });
</script>

</div>
</body>
</html>
