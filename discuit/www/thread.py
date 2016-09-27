# GPL v3 - MN Technique and contributors
import frappe

def get_context(context):
    thr = frappe.get_all("Thread", fields=["name", "th_thread_title"])
    thread_post_count = []
    for i in thr:
        thread_post_count.append({
            "name": i.name,
            "post_count": frappe.db.count("Post", filters={"pst_thread":i.name}),
            "thread_title": i.th_thread_title
        })
    context.threads = thread_post_count
    context.nocache = 1



    post  = frappe.get_doc('Post', frappe.form_dict.post)



    context.doc = post
    return context