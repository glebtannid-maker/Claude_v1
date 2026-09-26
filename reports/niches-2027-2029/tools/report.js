(function(){
  var t = document.getElementById('rank');
  if (!t) return;
  var tb = t.tBodies[0];
  var dir = {};
  t.tHead.querySelectorAll('th').forEach(function(th, idx){
    th.addEventListener('click', function(){
      var rows = Array.prototype.slice.call(tb.rows);
      var num = th.classList.contains('num');
      var d = dir[idx] = -(dir[idx] || (num ? 1 : -1));
      rows.sort(function(a, b){
        var x = a.cells[idx].getAttribute('data-v') || a.cells[idx].textContent;
        var y = b.cells[idx].getAttribute('data-v') || b.cells[idx].textContent;
        if (num) { x = parseFloat(x) || 0; y = parseFloat(y) || 0; return (x - y) * d; }
        return String(x).localeCompare(String(y), 'ru') * d;
      });
      rows.forEach(function(r){ tb.appendChild(r); });
      t.tHead.querySelectorAll('th').forEach(function(h){ h.classList.remove('sorted'); });
      th.classList.add('sorted');
    });
  });
  document.querySelectorAll('.flt').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.flt').forEach(function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.getAttribute('data-f');
      Array.prototype.forEach.call(tb.rows, function(r){
        r.hidden = !(f === 'all' || r.getAttribute('data-type') === f);
      });
    });
  });
})();
