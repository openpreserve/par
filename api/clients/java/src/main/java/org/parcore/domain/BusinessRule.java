package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.threeten.bp.OffsetDateTime;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * A Business Rule describes additional context asserting how a Preservation Action should be performed. This allows the author of the rule to specify for example, a priority order in which to attempt certain Preservation Actions on particular content types, which inputs to supply, which outputs to extract etc. It also allows some free text fields to provide justification or share experience.
 */
@SuppressWarnings("unused")
@ApiModel(description = "A Business Rule describes additional context asserting how a Preservation Action should be performed. This allows the author of the rule to specify for example, a priority order in which to attempt certain Preservation Actions on particular content types, which inputs to supply, which outputs to extract etc. It also allows some free text fields to provide justification or share experience.")
public class BusinessRule {

    @SerializedName("description")
    private String description = null;

    @SerializedName("formatFamilies")
    private List<FormatFamily> formatFamilies = null;

    @SerializedName("formats")
    private List<ParIdentifier> formats = null;

    @SerializedName("id")
    private ParIdentifier id = null;

    @SerializedName("localLastModifiedDate")
    private OffsetDateTime localLastModifiedDate = null;

    @SerializedName("notes")
    private String notes = null;

    @SerializedName("preservationActionTypes")
    private List<PreservationActionType> preservationActionTypes = null;

    @SerializedName("preservationActions")
    private List<Action> preservationActions = null;

    /**
     * A short human readable explanation/display name for the Business Rule, e.g. &#39;Use md5sum to perform the MD5Check Preservation Action for all files&#39;
     * @return description
     **/
    @ApiModelProperty(value = "A short human readable explanation/display name for the Business Rule, e.g. 'Use md5sum to perform the MD5Check Preservation Action for all files'")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void addFormatFamiliesItem(FormatFamily formatFamiliesItem) {
        if (this.formatFamilies == null) {
            this.formatFamilies = new ArrayList<FormatFamily>();
        }
        this.formatFamilies.add(formatFamiliesItem);
    }

    /**
     * A list of format families that this Business Rule should be applied to
     * @return formatFamilies
     **/
    @ApiModelProperty(value = "A list of format families that this Business Rule should be applied to")
    public List<FormatFamily> getFormatFamilies() {
        return formatFamilies;
    }

    public void setFormatFamilies(List<FormatFamily> formatFamilies) {
        this.formatFamilies = formatFamilies;
    }

    public void addFormatsItem(ParIdentifier formatsItem) {
        if (this.formats == null) {
            this.formats = new ArrayList<ParIdentifier>();
        }
        this.formats.add(formatsItem);
    }

    /**
     * A list of file formats that this Business Rule should be applied to
     * @return formats
     **/
    @ApiModelProperty(value = "A list of file formats that this Business Rule should be applied to")
    public List<ParIdentifier> getFormats() {
        return formats;
    }

    public void setFormats(List<ParIdentifier> formats) {
        this.formats = formats;
    }

    /**
     * Get id
     * @return id
     **/
    @ApiModelProperty(required = true, value = "")
    public ParIdentifier getId() {
        return id;
    }

    public void setId(ParIdentifier id) {
        this.id = id;
    }

    /**
     * Get localLastModifiedDate
     * @return localLastModifiedDate
     **/
    @ApiModelProperty(value = "")
    public OffsetDateTime getLocalLastModifiedDate() {
        return localLastModifiedDate;
    }

    public void setLocalLastModifiedDate(OffsetDateTime localLastModifiedDate) {
        this.localLastModifiedDate = localLastModifiedDate;
    }

    /**
     * A free text field for providing additional context. This may be used to record the decision making process that led to the formulation of this rule, details of real-world experience in applying the rule, or any other text.
     * @return notes
     **/
    @ApiModelProperty(value = "A free text field for providing additional context. This may be used to record the decision making process that led to the formulation of this rule, details of real-world experience in applying the rule, or any other text.")
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public void addPreservationActionTypesItem(PreservationActionType preservationActionTypesItem) {
        if (this.preservationActionTypes == null) {
            this.preservationActionTypes = new ArrayList<PreservationActionType>();
        }
        this.preservationActionTypes.add(preservationActionTypesItem);
    }

    /**
     * A list of Preservation Action Types that this Business Rule should be applied to. This might be a subset of those that the Preservation Actions themselves apply to. For example, a file format transformation action might itself apply to Migration and Normalization action types, but the Business Rule might be applicable only to Normalization
     * @return preservationActionTypes
     **/
    @ApiModelProperty(value = "A list of Preservation Action Types that this Business Rule should be applied to. This might be a subset of those that the Preservation Actions themselves apply to. For example, a file format transformation action might itself apply to Migration and Normalization action types, but the Business Rule might be applicable only to Normalization")
    public List<PreservationActionType> getPreservationActionTypes() {
        return preservationActionTypes;
    }

    public void setPreservationActionTypes(List<PreservationActionType> preservationActionTypes) {
        this.preservationActionTypes = preservationActionTypes;
    }

    public void addPreservationActionsItem(Action preservationActionsItem) {
        if (this.preservationActions == null) {
            this.preservationActions = new ArrayList<Action>();
        }
        this.preservationActions.add(preservationActionsItem);
    }

    /**
     * A list of specific actions. These are defined internally to reference the Core Preservation Action, the priority order in which it should be performed, and any inputs and outputs that should be used.
     * @return preservationActions
     **/
    @ApiModelProperty(value = "A list of specific actions. These are defined internally to reference the Core Preservation Action, the priority order in which it should be performed, and any inputs and outputs that should be used.")
    public List<Action> getPreservationActions() {
        return preservationActions;
    }

    public void setPreservationActions(List<Action> preservationActions) {
        this.preservationActions = preservationActions;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        BusinessRule businessRule = (BusinessRule) o;
        return Objects.equals(this.description, businessRule.description) &&
                Objects.equals(this.formatFamilies, businessRule.formatFamilies) &&
                Objects.equals(this.formats, businessRule.formats) &&
                Objects.equals(this.id, businessRule.id) &&
                Objects.equals(this.localLastModifiedDate, businessRule.localLastModifiedDate) &&
                Objects.equals(this.notes, businessRule.notes) &&
                Objects.equals(this.preservationActionTypes, businessRule.preservationActionTypes) &&
                Objects.equals(this.preservationActions, businessRule.preservationActions);
    }

    @Override
    public int hashCode() {
        return Objects.hash(description, formatFamilies, formats, id, localLastModifiedDate, notes, preservationActionTypes, preservationActions);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class BusinessRule {\n");

        sb.append("    description: ").append(toIndentedString(description)).append("\n");
        sb.append("    formatFamilies: ").append(toIndentedString(formatFamilies)).append("\n");
        sb.append("    formats: ").append(toIndentedString(formats)).append("\n");
        sb.append("    id: ").append(toIndentedString(id)).append("\n");
        sb.append("    localLastModifiedDate: ").append(toIndentedString(localLastModifiedDate)).append("\n");
        sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
        sb.append("    preservationActionTypes: ").append(toIndentedString(preservationActionTypes)).append("\n");
        sb.append("    preservationActions: ").append(toIndentedString(preservationActions)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
