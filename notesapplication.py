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
            return note_id,self.note_list[note_id],self.author
        
    def get_note(self, note_id):
    	return str(self.note_list[note_id])
    
    def search(self, search_text):
        for content in range(len(self.note_list)):
            if search_text in self.note_list[content]:
                
                return search_text, self.note_list[content]            
        
    def edit_notes(self, note_id, new_content):
        self.note_list[note_id] = new_content
        return self.note_list[note_id]

lolo_notes = NotesApplication("Lolo")

lolo_notes.create("Lolo is fun")
lolo_notes.create("She talks alot")

print lolo_notes.notes()
print lolo_notes.get_note(1)
print lolo_notes.search("lo")
print lolo_notes.edit_notes(0, "Lolo is boring")