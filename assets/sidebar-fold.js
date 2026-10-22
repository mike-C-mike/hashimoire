/* Hashimoire Docsify v4 sidebar folding.
   Uses the existing nested Markdown groups, not a separate navigation file.
   Keeps category state across Docsify route changes; accessible keyboard buttons.
*/
(function () {
  'use strict';

  var STORAGE_KEY = 'hashimoire.sidebar.groups.v1';
  function readState() {
    try {
      var parsed = JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '{}');
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (err) { return {}; }
  }
  var states = readState();

  function saveState() {
    try { window.localStorage.setItem(STORAGE_KEY, JSON.stringify(states)); }
    catch (err) { /* Browsers may disable local storage; toggles still work. */ }
  }
  function directChild(element, tag) {
    return Array.prototype.find.call(element.children, function (child) {
      return child.tagName === tag;
    });
  }
  function setExpanded(group, button, menu, expanded, label) {
    group.classList.toggle('hash-fold-closed', !expanded);
    button.setAttribute('aria-expanded', String(expanded));
    button.setAttribute('aria-label', (expanded ? 'Collapse ' : 'Expand ') + label);
    menu.hidden = !expanded;
  }
  function installGroups() {
    var sections = document.querySelectorAll('.sidebar-nav > ul > li');
    Array.prototype.forEach.call(sections, function (group, index) {
      var menu = directChild(group, 'UL');
      if (!menu || directChild(group, 'BUTTON')) return;
      var heading = directChild(group, 'STRONG') || directChild(group, 'P');
      var label = heading ? heading.textContent.replace(/\s+/g, ' ').trim() : 'Section ' + (index + 1);
      var key = label.toLowerCase();
      var active = !!menu.querySelector('li.active, a.active');
      var expanded = Object.prototype.hasOwnProperty.call(states, key) ? !!states[key] : active;
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'hash-fold-toggle';
      button.setAttribute('aria-controls', 'hash-side-group-' + index);
      button.title = 'Toggle ' + label;
      menu.id = 'hash-side-group-' + index;
      group.classList.add('hash-fold-group');
      group.insertBefore(button, group.firstChild);
      setExpanded(group, button, menu, expanded, label);
      button.addEventListener('click', function (event) {
        event.preventDefault();
        event.stopPropagation();
        var next = button.getAttribute('aria-expanded') !== 'true';
        states[key] = next;
        saveState();
        setExpanded(group, button, menu, next, label);
      });
      // The category heading is also a large touch/click target.
      if (heading && heading.tagName === 'STRONG') {
        heading.classList.add('hash-fold-heading');
        heading.setAttribute('title', 'Toggle ' + label);
        heading.setAttribute('tabindex', '0');
        heading.setAttribute('role', 'button');
        heading.addEventListener('click', function () { button.click(); });
        heading.addEventListener('keydown', function (event) {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            button.click();
          }
        });
      }
    });
  }

  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat(function (hook) {
    hook.ready(installGroups);
    hook.doneEach(function () {
      window.requestAnimationFrame(installGroups);
    });
  });
}());
