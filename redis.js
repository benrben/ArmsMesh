var redis = require ('redis')
var client = redis.createClient()
client.on('connect', function() {
    console.log('Redis client connected');
});

client.on('error', function (err) {
    console.log('Something went wrong ' + err);
});

// F:1,|G:y:71,x:190|,D:0,T:1550953170
// F:1,|P:98|,D:0,T:1550953170
// F:1,|A:y:149,x:194,z:185|,D:0,T:1550953170
var st ="F:1,|A:y:149,x:194,z:185|,D:0,T:1550953170";
var size = st.length+1;
var from="";
var i = 0 ;
var GPSX="";
var GPSY="";
var ACCX="";
var ACCY="";
var ACCZ="";
var Pulse="";
var time="";

while (size--){
    if (st.charAt(i)=='F'){
        i=i+2;
        size=size-2;
        from = st.charAt(i)
        if(!st.charAt(i++)==','){
            i++;
            size--;
            from+=st.charAt(i)
        }
        if(!st.charAt(i++)==','){
            i++
            size--
            from+=st.charAt(i)
        }
    }
    if(st.charAt(i)=='|'){
        i++
        size--
        if(st.charAt(i)=='G'){
            while(st.charAt(i)!='|'){
                i++
                size--
                if(st.charAt(i)=='y'){
                    i=i+2
                    size=size-2
                    while(st.charAt(i)!=","){
                        GPSY +=st.charAt(i);
                        i++
                        size--
                    }
                }
                if(st.charAt(i)=='x'){
                    i=i+2
                    size=size-2
                    while(st.charAt(i)!='|'){
                        GPSX+=st.charAt(i);
                        i++
                        size--
                    }
                }
            }
        }
        if(st.charAt(i)=='P'){
          size=size-2
          i=i+2
          while(st.charAt(i)!="|"){
              Pulse+=st.charAt(i)
              i++
          }
        }
        if(st.charAt(i)=='A'){
            while(st.charAt(i)!='|'){
                i++
                size--
                if(st.charAt(i)=='y'){
                    i=i+2
                    size=size-2
                    while(st.charAt(i)!=","){
                        ACCY +=st.charAt(i);
                        i++
                        size--
                    }
                }
                if(st.charAt(i)=='x'){
                    i=i+2
                    size=size-2
                    while(st.charAt(i)!=','){
                        ACCX+=st.charAt(i);
                        i++
                        size--
                    }
                }
                if(st.charAt(i)=='z'){
                    i=i+2
                    size=size-2
                    while(st.charAt(i)!='|'){
                        ACCZ+=st.charAt(i);
                        i++
                        size--
                    }
                }
        }
            if(st.charAt(i)=='E'){
               while(st.charAt(i)=='|'){
               }
            }
        }

        }
        if(st.charAt(i)=='T'){
            size=size-2
            i=i+2
            while(size--){
                time+=st.charAt(i)
                i++
            } 
        }
        i++
        if(size<=0){
            break
        }
        console.log(st.charAt(i))
}
console.log(from,GPSX,GPSY,time,Pulse,ACCX,ACCY,ACCZ)
var data = "{x:"+ACCX+",y:"+ACCY+"z:"+ACCZ+"}";
client.lpush("Sold::"+from+"::ACC::"+time,"Time:"+time+"|"+data)
client.expire("Sold::"+from+"::ACC::"+time,100)
// client.set('my test key', 'my test value', redis.print);
// client.get('my test key', function (error, result) {
//     if (error) {
//         console.log(error);
//         throw error;
//     }
//     console.log('GET result ->' + result);
// });
