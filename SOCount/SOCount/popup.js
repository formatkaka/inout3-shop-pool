// Update the relevant fields with the new data
function setDOMInfo(info) {
  document.getElementById('pname').textContent   = info.pname;
  document.getElementById('price').textContent  = info.price;
  document.getElementById('buttons').textContent = info.buttons;
}

// Once the DOM is ready...
window.addEventListener('DOMContentLoaded', function () {
  // ...query for the active tab...
  chrome.tabs.query({
    active: true,
    currentWindow: true
  }, function (tabs) {
    // ...and send a request for the DOM info...

    chrome.tabs.sendMessage(
        tabs[0].id,
        {from: 'popup', subject: 'DOMInfo'},
        // ...also specifying a callback to be called 
        //    from the receiving end (content script)
        setDOMInfo);
    document.getElementById('pageurl').textContent = tabs[0].url;
  });

  //check for local storage values

});

window.onload = function(){

    document.getElementById("registeruser").onclick=function(){
      var cname = document.getElementById("cname").value;
      var cemail = document.getElementById("cemail").value;
      var cmobno = document.getElementById("cmobno").value;
      var caddress = document.getElementById("caddress").value;
      alert("Hello "+cname);
      var storage = chrome.storage.local;
      var obj = {};
      obj["cname"] = cname;
      obj["cemail"] = cemail;
      obj["cmobno"] = cmobno;
      obj["caddress"] = caddress;
      chrome.storage.local.set(obj, function() {
    if (chrome.runtime.error) {
      console.log("Runtime error.");
    }
  });
}

  //document.body.onload = function()
  //{
    var storage = chrome.storage.local;

    var data_arr= [];
    storage.get('cname',function(result){
      console.log(result["cname"]);
      data_arr.push(result["cname"]);
    });
    storage.get('cemail',function(result){
      console.log(result["cemail"]);
      data_arr.push(result["cemail"]);
    });
    storage.get('cmobno',function(result){
      console.log(result["cmobno"]);
      data_arr.push(result["cmobno"]);
    });
    storage.get('caddress',function(result){
      console.log(result["caddress"]);
      data_arr.push(result["caddress"]);
      console.log(data_arr.length);
      if(data_arr[0])
      {
        document.getElementById("infotable").style.display = "block";
        document.getElementById("register").style.display = "none";
        document.getElementById("cname").textContent = data_arr[0];
        document.getElementById("cemail").textContent = data_arr[1];
        document.getElementById("caddress").textContent = data_arr[3];
      }
    });

    
  //}

}