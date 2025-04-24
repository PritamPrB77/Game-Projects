let p = document.querySelector(".box");
    let reset = document.querySelector(".reset");
    let ne = document.querySelector(".new-game");
    let ms = document.querySelector("#kk");
    let v = document.querySelectorAll(".buttom")
    console.log(p)
    let o = true;
    let count=0;
    let i;
    let winningpattern =
        [[0, 1, 2],
        [0, 3, 6],
        [0, 4, 8],
        [1, 4, 7],
        [2, 5, 8],
        [2, 4, 6],
        [3, 4, 5],
        [6, 7, 8],

        ];
  
    let showwinner = (s) => {
        //  ms.style.display= "block";
        ms.innerHTML = `congratulation winnier is ${s} `;
    }

    let gamedraw = () => {
        console.log("hello")
        ms.innerHTML = `game is draw`;
        for (let i of v) {
            i.disabled = true;

        }

    }

    let checkwinner = () => {
        //    for(let h=0;h<winningpattern.length;h++){
        //     for(let l=0;l<winningpattern[h].length;l++){
        //     //    console.logv[(winningpattern[h][l])
        //     console.log(v[winningpattern[h][l]].innerHTML);

        //     }
        //    }

        for (let pattern of winningpattern) {
            let x = v[pattern[0]].innerHTML;
            let y = v[pattern[1]].innerHTML;
            let z = v[pattern[2]].innerHTML;
            // let x=pattern[0]
            // let y=pattern[1]
            // let z=pattern[2]
            // console.log(x)
            if (x != "" && y != "" && z != "") {
                if (x == y && y == z) {
                    showwinner(x);
                    for (let i of v) {
                        i.disabled = true;

                    }
                    return true;
                }
            }
            return false;

        }
    }
    let newgane = () => {
        console.log("hi")
        ms.innerHTML = "";
        for (let i of v) {
            i.disabled = false;
        i.innerHTML = "";
        }
          


    }



    let box = (event) => {

        if (event.target.classList.contains("buttom")) {


            if (o) {
                i = event.target.innerHTML = `O`;
                o = false;
                event.target.disabled = true;
            }
            else {
                i = event.target.innerHTML = `X`;
                o = true;
                event.target.disabled = true;
            }


            count++;
            console.log(count)
            let isWinner = checkwinner();
            if (count == 9 && !isWinner) {
                gamedraw();
            }
        }


    }
    /*   v.forEach((bo)=> {
        
      bo.addEventListener("click",box);
    });*/
    //we can use for each also we dont need to write the baocve condition
    p.addEventListener("click", box)


    ne.addEventListener("click", newgane);

    reset.addEventListener("click", (event) => {
        console.log("hello")
        ms.innerHTML = "";
        for (let i of v) {
            i.disabled = false;
            i.innerHTML = "";
        }


    })
