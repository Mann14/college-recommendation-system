@app.route('/roadmap')
def roadmap():
    # Retrieve 'b1' from the session
    b1 = session.get('b1', '')
    roadmap_data = roadmaps.get(b1, {})  # Get the roadmap data for the branch
    print("Roadmap Data:", roadmap_data) 
    return render_template('roadmap.html', b1 = b1, roadmapData=roadmap_data, roadmaps = roadmaps)