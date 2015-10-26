/* ***********************************************
 * Module to select export filter properties. Is currently
 * only responsible for dynamically populating the category
 * values for the category select and is automatically loaded
 * when included in a page.
 *
 * @author Patrick Rickles (http://github.com/excites)
 * @version 0.1
 * ***********************************************/

 $(function() {
    'use strict';

    $('select[name=checklists]').on('change', function () {
        var selectedChecklistId = $(this).val();
        var project_input = $('input[name=checklist-project-id]');
        var project_id = project_input.val();
        if(project_id == "")
        {
          //not the most robust method...
          project_id = 999999;
          project_input.val(project_id);
        }

        var checklistSettingsLink = $('[name=checklist-settings]');
        checklistSettingsLink.attr('href', '/admin/checklist/settings/' + project_id + '/');

        var checklistAddChecklistLink = $('[name=checklist-add-checklist-link]');
        checklistAddChecklistLink.attr('href', '/admin/checklist/add-checklist/' + project_id + '/');

        var category_id = -1;

        var checklistItemsTableExpired = $('table[name=checklist-items-expired]');
        checklistItemsTableExpired.find("tr:gt(0)").remove();

        var checklistItemsTableExpiringSoon = $('table[name=checklist-items-expiring-soon]');
        checklistItemsTableExpiringSoon.find("tr:gt(0)").remove();

        var checklistItemsTableEssential = $('table[name=checklist-items-essential]');
        checklistItemsTableEssential.find("tr:gt(0)").remove();

        var checklistItemsTableUseful = $('table[name=checklist-items-useful]');
        checklistItemsTableUseful.find("tr:gt(0)").remove();

        var checklistItemsTablePersonal = $('table[name=checklist-items-personal]');
        checklistItemsTablePersonal.find("tr:gt(0)").remove();

        var checklistItemsTableChildren = $('table[name=checklist-items-children]');
        checklistItemsTableChildren.find("tr:gt(0)").remove();

        var checklistItemsTableToddlers = $('table[name=checklist-items-toddlers]');
        checklistItemsTableToddlers.find("tr:gt(0)").remove();

        var checklistItemsTableInfants = $('table[name=checklist-items-infants]');
        checklistItemsTableInfants.find("tr:gt(0)").remove();

        var checklistItemsTablePets = $('table[name=checklist-items-pets]');
        checklistItemsTablePets.find("tr:gt(0)").remove();

        var checklistItemsTableCustom = $('table[name=checklist-items-custom]');
        checklistItemsTableCustom.find("tr:gt(0)").remove();

        var checklistDescriptions = $('div[name=checklist-descriptions]');
        var cd_divs = checklistDescriptions.children("div");
        for(var i = 0; i < cd_divs.length; i++)
        {
          var cd_div = cd_divs[i];
          var cd_div_name = cd_div.getAttribute('name');

          if(cd_divs.length == 1)
          {
            //no checklists, so show the empty description
            cd_div.setAttribute('style', 'display:block');
          }
          else {
            if(cd_div_name == "checklist-description"+selectedChecklistId)
            {
              cd_div.setAttribute('style', 'display:block');
            }
            else {
              cd_div.setAttribute('style', 'display:none');
            }
          }
        }

        var expired_div = $('div[name=checklist-items-expired-div]');
        expired_div.hide();
        var expiring_soon_div = $('div[name=checklist-items-expiring-soon-div]');
        expiring_soon_div.hide();

        var essential_div = $('div[name=checklist-items-essential-div]');
        essential_div.hide();
        var useful_div = $('div[name=checklist-items-useful-div]');
        useful_div.hide();
        var personal_div = $('div[name=checklist-items-personal-div]');
        personal_div.hide();
        var children_div = $('div[name=checklist-items-children-div]');
        children_div.hide();
        var toddlers_div = $('div[name=checklist-items-toddlers-div]');
        toddlers_div.hide();
        var infants_div = $('div[name=checklist-items-infants-div]');
        infants_div.hide();
        var pets_div = $('div[name=checklist-items-pets-div]');
        pets_div.hide();
        var custom_div = $('div[name=checklist-items-custom-div]');
        custom_div.hide();

        if(selectedChecklistId) {
            $.get('/admin/checklist/' + project_id + '/' + selectedChecklistId + '/items/', function (new_items) {
                if(new_items) {
                    var new_items_p = $.parseJSON(new_items);

                    for (var key in new_items_p) {

                        if (new_items_p.hasOwnProperty(key)) {
                          var cid_obj = new_items_p[key];

                          var id = -1;
                          var name = "";
                          var have_it = false;
                          var quantity = -1;
                          var expiry = Date.now();
                          var checklistitemtype = "";

                          for(var key2 in cid_obj) {
                            //alert(key2 + " : " + cid_obj[key2] + " : " + typeof(cid_obj[key2]));
                            switch(key2) {
                              case "id":
                                id = cid_obj[key2];
                                break;

                              case "name":
                                name = cid_obj[key2];
                                break;

                              case "quantity":
                                quantity = cid_obj[key2];
                                break;

                              case "expiry":
                                expiry = cid_obj[key2];
                                break;

                              case "haveit":
                                have_it = cid_obj[key2];
                                break;

                              case "category_id":
                                category_id = cid_obj[key2];
                                break;

                              case "checklistitemtype":
                                  checklistitemtype = cid_obj[key2];
                                  break;

                              default:
                                //do nothing
                            }
                          }

                          //alert("id:" + id + " name:" + name);

                          //if(name == "Fixit") {
                          //  var checklistFixitLink = $('[name=checklist-fixit-link]');
                          //  checklistFixitLink.attr('href','/admin/checklist/' + id + '/');
                          //}

                          var rowHTML = "<tr name='item" + id + "'>";

                          if(have_it) {
                            rowHTML += "<td>";
                            var update_url = "/admin/checklist/" + project_id + "/" + category_id + "/edit-item-val/" + id + "/" + "haveit" + "/" + "False" + "/";
                            rowHTML += "<form method='POST' action='" + update_url + "' name='form-haveit" + id + "' novalidate>";
                            var onchange_fcn_str = "updateCI(\"" + project_id + "\",\"" + category_id + "\",\"" + id + "\",\"" + "haveit" + "\",\"" + "False" + "\")";
                            rowHTML += "<input type='checkbox' name='haveit" + id + "' onchange='" + onchange_fcn_str + "' checked />";
                            rowHTML += "</form>";
                            rowHTML += "</td>";
                          }
                          else {
                            rowHTML += "<td>";
                            var update_url = "/admin/checklist/" + project_id + "/" + category_id + "/edit-item-val/" + id + "/" + "haveit" + "/" + "True" + "/";
                            rowHTML += "<form method='POST' action='" + update_url + "' name='form-haveit" + id + "' novalidate>";
                            var onchange_fcn_str = "updateCI(\"" + project_id + "\",\"" + category_id + "\",\"" + id + "\",\"" + "haveit" + "\",\"" + "True" + "\")";
                            rowHTML += "<input type='checkbox' name='haveit" + id + "' onchange='" + onchange_fcn_str + "' />";
                            rowHTML += "</form>";
                            rowHTML += "</td>";
                          }
                          rowHTML += "<td>" + name + "</td>";
                          rowHTML += "<td>" + quantity + "</td>";
                          rowHTML += "<td>" + expiry + "</td>";
                          rowHTML += "<td>" + checklistitemtype + "</td>";
                          rowHTML += "<td>" + "<a href='/admin/checklist/" + project_id + "/" + category_id + "/edit-item/" + id + "/' name='checklist-item-edit" + id + "' class='btn btn-primary'>Edit</a>" + "</td>";
                          rowHTML += "<td>" + "<a href='/admin/checklist/" + project_id + "/" + category_id + "/delete-item/" + id + "/' name='checklist-item-delete" + id + "' class='btn btn-primary'>Delete</a>" + "</td>";
                          rowHTML += "</tr>";

                          //if(expiry < now())
                          //{
                          //  expired_div.show();
                          //  checklistItemsTableExpired.append(rowHTML);
                          //}
                          //else if( expiry < (now() - 7) )
                          //{
                          //  expiring_soon_div.show();
                          //  checklistItemsTableExpiringSoon.append(rowHTML);
                          //}
                          //else {

                            switch(checklistitemtype)
                            {
                              case "Essential":
                                essential_div.show();
                                checklistItemsTableEssential.append(rowHTML);
                                break;

                              case "Useful":
                                useful_div.show();
                                checklistItemsTableUseful.append(rowHTML);
                                break;

                              case "Personal":
                                personal_div.show();
                                checklistItemsTablePersonal.append(rowHTML);
                                break;

                              case "Children":
                                children_div.show();
                                checklistItemsTableChildren.append(rowHTML);
                                break;

                              case "Toddlers":
                                toddlers_div.show();
                                checklistItemsTableToddlers.append(rowHTML);
                                break;

                              case "Infants":
                                infants_div.show();
                                checklistItemsTableInfants.append(rowHTML);
                                break;

                              case "Pets":
                                pets_div.show();
                                checklistItemsTablePets.append(rowHTML);
                                break;

                              case "Custom":
                                custom_div.show();
                                checklistItemsTableCustom.append(rowHTML);
                                break;
                              default:
                                //do nothing
                              }
                            //}
                        }
                    }
                }

                category_id = $('select[name=checklists]').val();
                var checklistAddItemLink = $('[name=checklist-add-item-link]');
                checklistAddItemLink.attr('href', '/admin/checklist/' + project_id + '/' + category_id +'/add-item/');

                var checklistEditChecklistLink = $('[name=checklist-edit-checklist-link]');
                checklistEditChecklistLink.attr('href', '/admin/checklist/' + project_id + '/edit-checklist/' + category_id + '/');

                var checklistDeleteChecklistLink = $('[name=checklist-delete-checklist-link]');
                checklistDeleteChecklistLink.attr('href', '/admin/checklist/' + project_id + '/delete-checklist/' + category_id + '/');

            });

        }

     }).trigger('change');

    $(document).ready(function() {
      $('select[name=checklist-items]').change();
    });
 });

function updateCI(project_id, category_id, ci_id, item_key, new_val){
  //var page_url = "/admin/checklist/" + project_id + "/";
  var update_url = "/admin/checklist/" + project_id + "/" + category_id + "/edit-item-val/" + ci_id + "/" + item_key + "/" + new_val + "/";
  //alert(update_url);
  //This is throwing a CSRF token forbidden issue
  //$("form[name=form-haveit" + ci_id +"]").submit();

  //I'm getting an out of memory exception in the browser console here, but it's working so I'll come back to this later.
  window.location.href = update_url;

  //I think this is the right way to do this, but I'm not sure how to implement this.
  //There's also similar functionality in geokey/static/js/admin.control.ajax.js, but not sure how to tap into it...

  //$.ajax({ url: page_url,
  //  type: 'POST',
  //  beforeSend: function(xhr) {xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'))},
  //  data: '',
  //  success: function(response) {
      //$("form[name=form-haveit" + ci_id +"]").submit();
      //window.location.href = update_url;
  //  }
  //});

}
