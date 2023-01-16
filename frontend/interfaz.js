window.onload = function(){
    const API_URL = "http://localhost:5000";

    fetch(API_URL+'/getPopulation')
        .then((response) => response.json())
        .then(colors =>{


        let currentColorIndex = -2;
        let changeColorButton1 = document.getElementById("change-color-button");
        let changeColorButton2 = document.getElementById("change-color-button2");


        changeColorButton1.addEventListener("click", function () {
            currentColorIndex = currentColorIndex + 2;
            if (currentColorIndex >= 20) {
                console.log(colors)
                postData("http://localhost:5000/trainPopulation", colors).
                then(response => {
                    colors = response;
                    console.log("Nueva generación")
                    update_colors(255,255,255,255,255,255)
                    console.log(colors)
                    currentColorIndex = -2;                    
                })
            }else{
                let h = colors[currentColorIndex]['h'];
                let s = colors[currentColorIndex]['s'];
                let l = colors[currentColorIndex]['l'];
                let h2 = colors[currentColorIndex+1]['h'];
                let s2 = colors[currentColorIndex+1]['s'];
                let l2 = colors[currentColorIndex+1]['l'];
                colors[""+currentColorIndex+""].f = 1;
                hsv1 = HSVtoRGB(h,s,l)
                hsv2 = HSVtoRGB(h2,s2,l2)
                update_colors(hsv1['r'],hsv1['g'],hsv1['b'],hsv2['r'],hsv2['g'],hsv2['b']);

            }

        });

        changeColorButton2.addEventListener("click", function () {
            currentColorIndex = currentColorIndex + 2;
            if (currentColorIndex >= 20) {
                console.log(colors)
                postData("http://localhost:5000/trainPopulation", colors).
                then(response => {
                    colors = response;
                    console.log("Nueva generación")
                    update_colors(255,255,255,255,255,255)
                    console.log(colors)
                    currentColorIndex = -2;
                })
            }else{
                let h = colors[currentColorIndex]['h'];
                let s = colors[currentColorIndex]['s'];
                let l = colors[currentColorIndex]['l'];
                let h2 = colors[currentColorIndex+1]['h'];
                let s2 = colors[currentColorIndex+1]['s'];
                let l2 = colors[currentColorIndex+1]['l'];
                colors[""+(currentColorIndex+1)+""].f = 1;
                hsv1 = HSVtoRGB(h,s,l)
                hsv2 = HSVtoRGB(h2,s2,l2)
                update_colors(hsv1['r'],hsv1['g'],hsv1['b'],hsv2['r'],hsv2['g'],hsv2['b']);

            }

        });

        const button = document.getElementById("document");
        button.addEventListener("click", function () {
            var myDict = colors;
            var myDictString = JSON.stringify(myDict);
            localStorage.setItem("myDict", myDictString);

        window.location.href = "index2.html";
        });

        
            
    });

}

function HSVtoRGB(h, s, v) {
    h /= 360
    s /=100
    v /= 100
        var r, g, b, i, f, p, q, t;
        if (arguments.length === 1) {
            s = h.s, v = h.v, h = h.h;
        }
        i = Math.floor(h * 6);
        f = h * 6 - i;
        p = v * (1 - s);
        q = v * (1 - f * s);
        t = v * (1 - (1 - f) * s);
        switch (i % 6) {
            case 0: r = v, g = t, b = p; break;
            case 1: r = q, g = v, b = p; break;
            case 2: r = p, g = v, b = t; break;
            case 3: r = p, g = q, b = v; break;
            case 4: r = t, g = p, b = v; break;
            case 5: r = v, g = p, b = q; break;
        }
        return {
            r: Math.round(r * 255),
            g: Math.round(g * 255),
            b: Math.round(b * 255)
        };
    }

function postData(url, data) {
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .catch(error => console.error(error))
  }


function update_colors(h,s,l,h2,s2,l2){
    let colorBox = document.getElementById("color-box");
    let colorBox2 = document.getElementById("color-box2");
    colorBox.style.backgroundColor = "rgb("+h+", "+s+", "+l+")";
    colorBox2.style.backgroundColor = "rgb("+h2+", "+s2+", "+l2+")";
}
  







