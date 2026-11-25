fetch('/api/booking')
    .then(r => r.json())
    .then(r => {
        r.booking.forEach((b)=>{
            let div = document.createElement('div');
            div.innerHTML = `${b.whn}`
            document.body.append(div);
        })
    });

/* Build the add booking controls */
document.body.append(
    $m('div', {class: 'booking-controls'},[
        $m('h2', {}, 'Add Booking'),
        $m('label', ['When',$m('input', {id:'whn',value:'2026-11-26'})]),
        $m('label', ['Who', $m('input', {id:'who',value:'andrew'})]),
        $m('button',{onclick:()=>{
            let payload = {
                who:$i('who').value,
                whn:$i('whn').value
            }
            fetch('/api/booking',{
                method:'POST',
                body:JSON.stringify(payload),
                headers: {'Content-Type': 'application/json'}
            }).then(r=>r.json()).then(r=>{
                console.log('booking added',r)
            })
        }},'Make it so')
    ])
);