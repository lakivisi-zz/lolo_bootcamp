class NotesApplication(object):
    '''Note'''
    def __init__(self,author):
    	super(NotesApplication, self).__init__()
        self.author = author
        self.note_list= []

    
    def create(self,note_content):
       
        self.note_list.append(note_content)

    def notes(self):
        for note_id in range(len(self.note_list)):
            print "Note ID {} \n {}\n  By author {}".format(note_id,self.note_list[note_id],self.author)
        
    def get_note(self, note_id):
    	print str(self.note_list[note_id])
    
    def search(self, search_text):
        for content in range(len(self.note_list)):
            if search_text in self.note_list[content]:
                
                print "Search for ",search_text, "found in ", self.note_list[content]            
        
    def edit_notes(self, note_id, new_content):
        self.note_list[note_id] = new_content
        print self.note_list[note_id]

lolo_notes = NotesApplication("Lolo")
lolo_notes.create("Lolo is fun")
lolo_notes.create("She talks alot")
lolo_notes.notes()
lolo_notes.get_note(1)
lolo_notes.search("lo")
lolo_notes.edit_notes(0, "Lolo is boring")