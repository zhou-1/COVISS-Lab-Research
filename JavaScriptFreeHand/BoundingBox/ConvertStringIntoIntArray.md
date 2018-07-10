
        var linesbounding = data.bbList;    //string

        for (var i = 0, len = linesbounding.length; i < len; i++) {
        //alert( linesbounding[i])

        //convert from string to int array include comma
        var intbounding = linesbounding[i].split(",").map(Number);   //object

        //alert( intbounding[1])
        //alert(typeof intbounding[1])// number

        contexto.beginPath();
        contexto.rect(intbounding[0], intbounding[1], intbounding[2], intbounding[3]);
        //contexto.fillStyle = 'yellow';

