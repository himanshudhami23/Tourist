function fn_bindtostroage() {
    let strg = localStorage.getItem('dbmovie')
    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }

    var id = $('#txtId').val()
    let dt = strg.filter(function(e) {
        if (e.id == id) {
            return e
        }
    });
    if (dt.length <= 0) {

        var url = $('#txturl').val()
        var image = $('#txtimage').val()
        console.log(url, id)
        var name = $('#txtname').text()
        var category = $('#txtcatrgory').text()
        data = {
            'id': id,
            'url': url,
            'name': name,
            'category': category,
            'image': image,
        }

        strg.push(data)
        window.localStorage.setItem('dbmovie', JSON.stringify(strg))
    }
}

function fn_bind_time(time, price) {

    let strg = localStorage.getItem('dbmovie')
    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }

    strg[0]['time'] = time
    strg[0]['price'] = price

    window.localStorage.setItem('dbmovie', JSON.stringify(strg))

    fn_redrictseat()

}

function fn_redrictseat() {
    let strg = localStorage.getItem('dbmovie')
    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }

    if (strg[0]['time'] != null) {

        window.location.assign('/movies/' + strg[0]['url'] + '/seatbook/')
    }

}

function fn_checkSeat() {
    lst = []
    let strg = localStorage.getItem('dbmovie')


    $.each($('.economy').find('input[type="checkbox"]:checked'), function() {

        eco_seat = $(this).prop('id')
        lst.push(eco_seat)

    })
    $.each($('.executive').find('input[type="checkbox"]:checked'),
        function() {
            console.log($(this).prop('id'))
            exe_seat = $(this).prop('name')
            lst.push(exe_seat)

        })

    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }

    strg[0]['seats'] = lst
    window.localStorage.setItem('dbmovie', JSON.stringify(strg))
    window.location.assign('/movies/' + strg[0]['url'] + '/ticket/')


}

function fn_redrictconfirmation() {
    let strg = localStorage.getItem('dbmovie')
    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }

    if (strg[0]['seat'] != null) {
        window.location.assign('/movies/' + strg[0]['url'] + '/ticket/')
    }
}

function fn_bindTicket() {
    let strg = localStorage.getItem('dbmovie')
    if (strg != null && strg != '""' && typeof strg != 'undefined') {
        strg = JSON.parse(strg);
    } else {
        strg = []
    }
    $('#spnTime,#spnTime2').text(strg[0]['time'])


    spn = ''
    total_ticket = strg[0]['seats'].length
    amt = parseFloat(total_ticket) * parseFloat(strg[0]['price'])
    gst_amt = amt * 18 / 100

    total_amt = parseFloat(amt) + parseFloat(gst_amt)

    total_amt = parseFloat(total_amt).toFixed(2)
    $('#spnTicket').text('[' + total_ticket + ' Tickets]')
    $('#snpTotalAmt').text(total_amt)
    $('#snpgst').text(gst_amt)
    $('#snpamt').text(amt)
    console.log(amt, gst_amt, total_amt)

    $.each(strg[0]['seats'], function() {

        spn += '<span>' + this + ' </span>,'
    })
    $('#spnSeats').append(spn)
    $('#spnSeats1').append(spn)
    strg[0]['grand_total'] = total_amt
    window.localStorage.setItem('dbmovie', JSON.stringify(strg))
}